#  This file will generate the asm code that will run

import c_ast
from STATS import *
from symbol_table import *

code_list = c_ast.getCode()
labels = {}
param_size = 0
func_param_size = 0
func_ret_size = 0
func_size = 0
func_name = ""

def fix_labels(code_list):
    for line in range(len(code_list)):

        if ( code_list[line][0][:2] =='if' or code_list[line][0]=='goto' ) and code_list[line][-1]:
            labels[str(code_list[line][-1])] = 1 


def has_label(ind):
    if str(ind) in labels:
        return 1
    else:
        return 0


#  Constants Handle the size

def getAddr(obj):
    if isinstance(obj, c_ast.TAC):
        refer = obj.refer
        if type(refer) == tuple:
            refer = getSTEntry(refer)
            print("[getAddr]")
            print(refer)
            offset = refer[2] 
            size = refer[3]
            return (offset, "addr", size)
        else:
            #  Handle Here Important replace 8 by size in .size
            return (int(refer), "const",  4)
    elif isinstance(obj, c_ast.Constant):
        return (int(obj.refer), "const", 4)
    return (int(obj), "const", 4)

def writeCode():
    param_size = 0
    fix_labels(code_list)

    file = open('assembly.asm', 'w')
    file.write(".data"+"\n")
    file.write('\tnewline: .asciiz "\\n"'+'\n')
    file.write('\tspace: .asciiz " "'+'\n')
    file.write(".text"+"\n")

    file.write("main:"+"\n")

    file.write("\tsub $sp, $sp, "+str(4)+"\n")
    #
    #  file.write("\tsub $sp, $sp, "+str(reg_size)+"\n")
    #  file.write("\tsw $s7, 0($sp)"+"\n")
    #  file.write("\tadd $s7, $zero, $sp"+"\n")
    #
    #  for i in range(6,-1,-1):
    #      offset = -1*(7-i)*reg_size
    #
    #      if i == 6:
    #          file.write("\tsw $ra, "+str(offset)+"($s7)"+"\n")
    #      else:
    #          file.write("\tsw $s"+str(i)+", "+str(offset)+"($s7)"+"\n")

    local_param_size = 0 
    
    #  entry = getSTEntry(line[2].refer)
    CST = getCST()
    entry = CST.lookupFullScope("main")

    size = entry[3]
    size = size - local_param_size - reg_size
    
    #  file.write("\tsub $sp, $sp, "+str(size)+"\n")

    file.write("\tjal "+"_main"+"\n")
    #  Handle for return value
    
    file.write("\tadd $sp, $sp, "+str(local_param_size)+"\n")

    #  if int(line[3][2]) > 0:
    file.write("\tlw $t1, 0($sp)"+"\n")
    file.write("\tadd $sp, $sp, "+str(4)+"\n")

        #  Handle the return address of all others
        #  ret_offset = getAddr(line[1])[0]
        #  file.write("\tsw $t1, "+str(ret_offset-param_size)+"($s7)"+"\n")

    #  file.write("\tli $v0, 1"+"\n")
    #  file.write("\tadd $a0, $zero, $t1"+"\n")
    #  file.write("\tsyscall"+"\n")

    file.write("\tli $v0, 10"+"\n")
    file.write("\tsyscall"+"\n")

    for ind, line in enumerate(code_list):
        
        if has_label(ind):
            file.write("L"+str(ind)+":"+"\n")


        op = line[0]
        #  print(line)

        #  Skipping unwanted if else and goto
        if ( op[:2] =='if' or op=='goto' ) and not line[-1]:
            pass

        elif op == "begin":
            #  print(line)
            addr = getSTEntry(line[2].refer)
            name = addr[0]
            param_size = addr[1].args_size
            print("[Begin]Print Param Size")
            print(param_size)
            #  print(name)
            if name == "main":
                file.write("_main:"+"\n")
            else:
                file.write(name+":"+"\n")

            file.write("\tsub $sp, $sp, "+str(reg_size)+"\n")
            file.write("\tsw $s7, 0($sp)"+"\n")
            file.write("\tadd $s7, $zero, $sp"+"\n")

            for i in range(6,-1,-1):
                offset = -1*(7-i)*reg_size
                
                if i == 6:
                    file.write("\tsw $ra, "+str(offset)+"($s7)"+"\n")
                else:
                    file.write("\tsw $s"+str(i)+", "+str(offset)+"($s7)"+"\n")

                #  file.write("\tsw $s"+str(i)+", "+str(offset)+"($s7)"+"\n")

            size = addr[3]
            size = size - param_size - reg_size
            
            name = entry[0]
           
            file.write("\tsub $sp, $sp, "+str(size)+"\n")

        elif op == "pushret":
            if line[2]>0:
                file.write("\tsub $sp, $sp, "+str(func_ret_size)+"\n")

        elif op == "push":
            addr = getAddr(line[2])
            if addr[1] == "const":
                file.write("\tadd $t0, $zero, "+str(addr[0])+"\n")
                file.write("\tsub $sp, $sp, "+str(addr[2])+"\n")
                file.write("\tsw $t0, 0($sp)"+"\n")
            else:
                file.write("\tsub $sp, $sp, "+str(addr[2])+"\n")
                file.write("\tlw $t0, "+str(param_size - addr[0] + reg_size - addr[2])+"($s7)"+"\n")
                file.write("\tsw $t0, 0($sp)"+"\n")

        elif op == "ScanInt":
            print("[WriteCode]ScanInt")
            
            addr = getAddr(line[1])

            file.write("\tlw $t0, "+str(param_size - addr[0] + reg_size - addr[2])+"($s7)"+"\n")

            file.write("\tli $v0, 5"+"\n")
            file.write("\tsyscall"+"\n")
            file.write("\tsw $v0, ($t0)"+"\n")

        elif op == "PrintSpace":
            print("[WriteCode]PrintSpace")

            file.write("\tli $v0, 4"+"\n")
            file.write("\tla $a0, space"+"\n")
            file.write("\tsyscall"+"\n")

        elif op == "PrintNewline":
            print("[WriteCode]PrintNewline")

            file.write("\tli $v0, 4"+"\n")
            file.write("\tla $a0, newline"+"\n")
            file.write("\tsyscall"+"\n")

        elif op == "PrintInt":
            print("[WriteCode]PrintInt")
            
            addr = getAddr(line[1])

            print("[PrintInt]IN PRINTINT")
            print(addr)
            file.write("\tlw $t0, "+str(param_size - addr[0] + reg_size - addr[2])+"($s7)"+"\n")

            file.write("\tli $v0, 1"+"\n")
            file.write("\tadd $a0, $zero, $t0"+"\n")
            file.write("\tsyscall"+"\n")

        elif op == "calling":
            id = line[1]
            name = id.name
            CST = getCST()
            entry = CST.lookupFT(name)
            if entry:
                func_param_size = entry[-1]
                type = entry[1]
                func_ret_size = getSize(type.type.type)
                print("[Calling]Got Params")
                print("func_param_size:"+str(func_param_size)+" func_ret_size:"+str(func_ret_size))
            else:
                assert False

            GST = getGST()
            entry = GST.lookupCurrentScope(name)
            if entry:
                func_size = entry[3]
                func_name = entry[0]
                print("[Calling]Got Params")
                print("func_size:"+str(func_size)+" func_name:"+str(func_name))
            else:
                assert False


        elif op == "call":
            #  file.write("\tsub $sp, $sp, "+str(reg_size)+"\n")
            #  file.write("\tsw $s7, 0($sp)"+"\n")
            #  file.write("\tadd $s7, $zero, $sp"+"\n")
            #
            #  for i in range(6,-1,-1):
            #      offset = -1*(7-i)*reg_size
            #
            #      if i == 6:
            #          file.write("\tsw $ra, "+str(offset)+"($s7)"+"\n")
            #      else:
            #          file.write("\tsw $s"+str(i)+", "+str(offset)+"($s7)"+"\n")
            #
            #      #  file.write("\tsw $s"+str(i)+", "+str(offset)+"($s7)"+"\n")
            #
            #  local_param_size = int(line[3][1])
            #
            #  print("[Call] In Call")
            #  print(line[2])
            #  print(line[2].refer)
            #  entry = getSTEntry(line[2].refer.refer)
 #
            #  size = entry[3]
            func_size = func_size - func_param_size - reg_size

            #  name = entry[0]
 #
            #  file.write("\tsub $sp, $sp, "+str(size)+"\n")
            file.write("\tjal "+name+"\n")
            #  Handle for return value
            
            file.write("\tadd $sp, $sp, "+str(func_param_size)+"\n")

            if int(func_ret_size) > 0:
                file.write("\tlw $t1, 0($sp)"+"\n")
                file.write("\tadd $sp, $sp, "+str(func_ret_size)+"\n")

                #  Handle the return address of all others
                addr = getAddr(line[1])
                ret_offset = addr[0]

                file.write("\tsw $t1, "+str(param_size - ret_offset + reg_size - addr[2])+"($s7)"+"\n")
            
        elif op == "return":
            #  Get Value of object
            addr = getAddr(line[1])
            if addr[1] == "const":
                offset = param_size + reg_size
                file.write("\tadd $t0, $zero, "+str(addr[0])+"\n")
                file.write("\tsw $t0, "+str(offset)+"($s7)"+"\n")
            else:
                offset = param_size + reg_size
                file.write("\tlw $t0, "+str(param_size - addr[0] + reg_size - addr[2])+"($s7)"+"\n")
                file.write("\tsw $t0, "+str(offset)+"($s7)"+"\n")
            
            file.write("\tadd $sp, $s7, "+str(reg_size)+"\n")
            for i in range(8):
                offset = -1*reg_size*(7-i)
                if i == 6:
                    file.write("\tlw $ra, "+str(offset)+"($s7)"+"\n")
                else:
                    file.write("\tlw $s"+str(i)+", "+str(offset)+"($s7)"+"\n")

            file.write("\tjr $ra"+"\n")

        elif op == "MOVADR":
            l_addr = getAddr(line[1])
            l_offset = l_addr[0]

            r_addr = getAddr(line[2])

            file.write("\tlw $t0, "+str(param_size - l_addr[0] + reg_size - l_addr[2])+"($s7)"+"\n")

            if r_addr[1] == "addr":
                file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
            else:
                file.write("\tadd $t1, $zero, "+str(r_addr[0])+"\n")

            file.write("\tsw $t1, ($t0)"+"\n")


        elif op == "=" :
            l_addr = getAddr(line[1])
            #  l_refer = getSTEntry(line[1].refer)
            #  l_offset = -1*refer[2]
            l_offset = l_addr[0]

            r1_addr = getAddr(line[2])

            if r1_addr[1] == "addr":
                file.write("\tlw $t0, "+str(param_size - r1_addr[0] + reg_size - r1_addr[2])+"($s7)"+"\n")
            else:
                print("[WriteCode]IN =")
                print(r1_addr[0])
                file.write("\tadd $t0, $zero, "+str(r1_addr[0])+"\n")

            file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")

        # binary operators
        elif op == "+" or op == "-" or op == "*" or op == "/" or op == "%":
            optype = "int"
            #  print(line)
            #  Assuming only constants in operands

            l_addr = getAddr(line[1])
            #  l_refer = getSTEntry(line[1].refer)
            #  l_offset = -1*refer[2]
            l_offset = l_addr[0]

            r1_addr = getAddr(line[2])
            r2_addr = getAddr(line[3])
            # 
            if optype == "int":
                if r1_addr[1] == "addr":
                    file.write("\tlw $t0, "+str(param_size - r1_addr[0] + reg_size - r1_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd $t0, $zero, "+r1_addr[0]+"\n")

                if r2_addr[1] == "addr":
                    file.write("\tlw $t1, "+str(param_size - r2_addr[0] + reg_size - r2_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd $t1, $zero, "+str(r2_addr[0])+"\n")

                if op == "+":
                   file.write("\tadd $t0, $t0, $t1"+"\n")
                elif op == "-":
                   file.write("\tsub $t0, $t0, $t1"+"\n")
                elif op == "*":
                   file.write("\tmul $t0, $t0, $t1"+"\n")               
                elif op == "/":
                   file.write("\tdiv $t0, $t0, $t1"+"\n")
                elif op == "%":
                   file.write("\tdiv $t2, $t0, $t1"+"\n")
                   file.write("\tmul $t2, $t2, $t1"+"\n")
                   file.write("\tsub $t0, $t0, $t2"+"\n")     
                file.write("\ts.s $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")

            elif optype == float:
                if r1_addr[1] == "addr":
                    file.write("\tl.s $f0, "+str(param_size - r1_addr[0] + reg_size - r1_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd.s $f0, $zero, "+r1_addr[0]+"\n")

                if r2_addr[1] == "addr":
                    file.write("\tl.s $f1, "+str(param_size - r2_addr[0] + reg_size - r2_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd.s $f1, $zero, "+str(r2_addr[0])+"\n")

                if op == "+":
                   file.write("\tadd.s $t0, $f0, $f1"+"\n")
                elif op == "-":
                   file.write("\tsub.s $t0, $f0, $f1"+"\n")
                elif op == "*":
                   file.write("\tmul.s $t0, $f0, $f1"+"\n")               
                elif op == "/":
                   file.write("\tdiv.s $t0, $f0, $f1"+"\n")
                elif op == "%":
                   file.write("\tdiv.s $t2, $f0, $f1"+"\n")
                   file.write("\tmul.s $t2, $f2, $f1"+"\n")
                   file.write("\tsub.s $t0, $f0, $f2"+"\n")
                file.write("\ts.s $f0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")



            print("[OP+]")
            print(l_offset)
            print(param_size)

        # relational operators
        elif op == "if<" or op == 'if<=' or op == 'if>' or op == 'if>=' or op == 'if==' or op == 'if!=':
            optype = "int"
            if optype == "int":
                #  print(line)
                #  Assuming only constants in operands
                l_addr = getAddr(line[1])
                r_addr = getAddr(line[2])
                l_offset = l_addr[0]

                #  l_refer = getSTEntry(line[1].refer)
                #  l_offset = -1*refer[2]
                if l_addr[1] == "addr":
                    file.write("\tlw $t0, "+str(param_size - l_addr[0] + reg_size - l_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd $t0, $zero, "+l_addr[0]+"\n")
                if r_addr[1] == "addr":
                    file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd $t1, $zero, "+r_addr[0]+"\n")
                branchTo = "L"+str(line[-1])

                if op == "if<":
                    file.write("\tblt $t0, $t1, " + branchTo+"\n")
                elif op == "if>":
                    file.write("\tbgt $t0, $t1, " + branchTo+"\n")
                elif op == "if<=":
                    file.write("\tble $t0, $t1, " + branchTo+"\n")
                elif op == "if>=":
                    file.write("\tbge $t0, $t1, " + branchTo+"\n")
                elif op == "if==":
                    file.write("\tbeq $t0, $t1, " + branchTo+"\n")
                elif op == "if!=":
                    file.write("\tbne $t0, $t1, " + branchTo+"\n")
                # print("[if<]")
                # print(line[-1])
                # print(branchTo)


            elif optype == "float":
                #  print(line)
                #  Assuming only constants in operands
                l_addr = getAddr(line[1])
                r_addr = getAddr(line[2])
                l_offset = l_addr[0]

                #  l_refer = getSTEntry(line[1].refer)
                #  l_offset = -1*refer[2]
                if l_addr[1] == "addr":
                    file.write("\tl.s $f0, "+str(param_size - l_addr[0] + reg_size - l_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd.s $f0, $zero, "+l_addr[0]+"\n")
                if r_addr[1] == "addr":
                    file.write("\tl.s $f1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd.s $f1, $zero, "+r_addr[0]+"\n")
                branchTo = "L"+str(line[-1])

                if op == "if<":
                    file.write("\tc.lt.s $f0, $f1")
                    file.write("bc1f " + branchTo+"\n")
                elif op == "if>":
                    file.write("\tc.le.s $f0, $f1")
                    file.write("\tbcf0 " + branchTo+"\n")
                elif op == "if<=":
                    file.write("\tc.le.s $f0, $f1")
                    file.write("bc1f " + branchTo+"\n")
                elif op == "if>=":
                    file.write("\tc.lt.s $f0, $f1")
                    file.write("bc0f " + branchTo+"\n")
                elif op == "if==":
                    file.write("\tc.eq.s $f0, $f1")
                    file.write("bc1f " + branchTo+"\n")
                elif op == "if!=":
                    file.write("\tc.eq.s $f0, $f1")
                    file.write("bc0f " + branchTo+"\n")
                # print("[if<]")
                # print(line[-1])
                # print(branchTo)


        # Unary operators
        elif op == "~":
            l_addr = getAddr(line[1])
            l_offset = l_addr[0]
            r_addr = getAddr(line[2])
            if r_addr[1] == "addr":
                file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
            else:
                file.write("\tadd $t0, $zero, "+l_addr[0]+"\n")
            file.write("\tnot $t0, $t1"+"\n")
            file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")

        elif op == "deref":
            optype = "int"
            l_addr = getAddr(line[1])
            l_offset = l_addr[0]
            r_addr = getAddr(line[2])
            file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
            if optype == "int":
                file.write("\tlw $t0, ($t1)"+"\n")
                file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")

            elif optype == "float":
                file.write("\tl.s $f0, ($f1)"+"\n")
                file.write("\ts.s $f0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")

        elif op == "&":
            optype = "int"
            l_addr = getAddr(line[1])
            l_offset = l_addr[0]
            r_addr = getAddr(line[2])

            if line[1].isArrayRef:
                t_elem = line[1].array_pointer
                t_addr = getAddr(t_elem)
                file.write("\tlw $t0, "+str(param_size - t_addr[0] + reg_size - t_addr[2]))
                file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")
            else: 
                file.write("\tadd $t0, $s7, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"\n")
                file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")
        elif op == "if":
            #  print(line)
            #  Assuming only constants in operands

            l_addr = getAddr(line[1])
            #  l_refer = getSTEntry(line[1].refer)
            #  l_offset = -1*refer[2]
            if l_addr[1] == "addr":
                file.write("\tlw $t0, "+str(param_size - l_addr[0] + reg_size - l_addr[2])+"($s7)"+"\n")
            else:
                file.write("\tadd $t0, $zero, "+str(l_addr[0])+"\n")
            branchTo = "L"+str(line[-1])
            file.write("\tbne $t0, $zero " + branchTo+"\n")
            # print("[if]")
            # print(line[-1])
            # print(branchTo)

        elif op == "goto":
            #  print(line)
            #  Assuming only constants in operands

            branchTo = "L"+str(line[-1])
            file.write("\tb " + branchTo+"\n")
            print("[goto]")
            print(line)
            print(branchTo)
    #  file.write("\tli $v0, 1"+"\n")
    #  file.write("\tlw $t1, 0($sp)"+"\n")
    #  file.write("\tadd $a0, $zero, $t1"+"\n")
    #  file.write("\tsyscall"+"\n")
    #



#  For push

            #  file.write("\tadd $t1, $zero, "+str(line[2])+"\n")
            #  file.write("\tadd $t2, $zero, "+str(line[3])+"\n")
            #  file.write("\tadd $sp, $sp, -4"+"\n")
            #  file.write("\tsw $t3, 0($sp)"+"\n")

