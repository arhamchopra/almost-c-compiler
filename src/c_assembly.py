#  This file will generate the asm code that will run on Spim using the command 
#  spim -file assembly.asm in the main folder

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

file = open('assembly.asm', 'w')

def fix_labels(code_list):
    for line in range(len(code_list)):

        if ( code_list[line][0][:2] =='if' or code_list[line][0]=='goto' ) and code_list[line][-1]:
            labels[str(code_list[line][-1])] = 1 

def has_label(ind):
    if str(ind) in labels:
        return 1
    else:
        return 0

def handle_data(data):
    GST = getGST()
    data = GST.table['cur_scope']
    print(data)
    for key in range(len(data)):
        if data[key][-1]:
            print(key)
            print(data[key])
            entry = data[key]
            print(entry)
            if isinstance(entry[1], c_ast.FuncDecl):
                pass
            elif isinstance(entry[1], c_ast.ArrayDecl):
                file.write("\t"+str(entry[0])+": .space "+str(entry[3])+"\n")
            elif isinstance(entry[1], c_ast.TypeDecl):
                if entry[1].type.type[-1] == "int":
                    file.write("\t"+str(entry[0])+": .word 0 \n")
                if entry[1].type.type[-1] == "float":
                    file.write("\t"+str(entry[0])+": .float 0.0 \n")
            elif isinstance(entry[1], c_ast.IdentifierType):
                if entry[1].type[-1] == "int":
                    file.write("\t"+str(entry[0])+": .word 0 \n")
                if entry[1].type[-1] == "float":
                    file.write("\t"+str(entry[0])+": .float 0.0 \n")



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
            is_global = refer[6]
            return (offset, "addr", size, is_global, refer[0])
        else:
            #  Handle Here Important replace 8 by size in .size
            return (int(refer), "const",  4, False, None)
    elif isinstance(obj, c_ast.Constant):
        return (int(obj.refer), "const", 4, False, None)
    return (int(obj), "const", 4, False, None )

def writeCode():
    GST = getGST()
    data = c_ast.getGlobalData()
    fix_labels(code_list)

    file.write(".data"+"\n")
    handle_data(data)
    file.write('\tnewline: .asciiz "\\n"'+'\n')
    file.write('\tspacebar: .asciiz " "'+'\n')
    file.write(".text"+"\n")
    file.write("main:"+"\n")
    file.write("\tsub $sp, $sp, "+str(4)+"\n")
    local_param_size = 0 
    
    CST = getCST()
    entry = CST.lookupFullScope("main")
    size = entry[3]
    size = size - local_param_size - reg_size
    file.write("\tjal "+"_main"+"\n")
    #  Handle for return value
    
    file.write("\tadd $sp, $sp, "+str(local_param_size)+"\n")

    #  for handling the exit call of main
    file.write("\tlw $t1, 0($sp)"+"\n")
    file.write("\tadd $sp, $sp, "+str(4)+"\n")
    file.write("\tli $v0, 10"+"\n")
    file.write("\tsyscall"+"\n")

    for ind, line in enumerate(code_list):
        if has_label(ind):
            file.write("L"+str(ind)+":"+"\n")
        op = line[0]

        #  Skipping unwanted if else and goto
        if ( op[:2] =='if' or op=='goto' ) and not line[-1]:
            pass

        elif op == "begin":
            addr = getSTEntry(line[2].refer)
            name = addr[0]
            param_size = addr[1].args_size
            print("[Begin]Print Param Size")
            print(param_size)
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
            size = addr[3]
            size = size - param_size - reg_size
            name = entry[0]
           
            file.write("\tsub $sp, $sp, "+str(size)+"\n")

        elif op == "pushret":
            if line[2]>0:
                file.write("\tsub $sp, $sp, "+str(func_ret_size)+"\n")

        elif op == "push":
            addr = getAddr(line[2])
            if addr[3]:
                file.write("\tsub $sp, $sp, "+str(addr[2])+"\n")
                file.write("\tlw $t0, "+str(addr[4])+"\n")
                file.write("\tsw $t0, 0($sp)"+"\n")
            else:
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

            if addr[3]:
                file.write("\tlw $t0, "+str(addr[4])+"\n")
            else:
                file.write("\tlw $t0, "+str(param_size - addr[0] + reg_size - addr[2])+"($s7)"+"\n")

            file.write("\tli $v0, 5"+"\n")
            file.write("\tsyscall"+"\n")
            file.write("\tsw $v0, ($t0)"+"\n")

        elif op == "PrintSpace":
            print("[WriteCode]PrintSpace")

            file.write("\tli $v0, 4"+"\n")
            file.write("\tla $a0, spacebar"+"\n")
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
            if addr[3]:
                file.write("\tlw $t0, "+str(addr[4])+"\n")
            else:
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
                func_name = entry[0]
                print("[Calling]Got Params")
                print("func_param_size:"+str(func_param_size)+" func_ret_size:"+str(func_ret_size))
            else:
                assert False

        elif op == "call":
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
            if addr[3]:
                offset = param_size + reg_size
                file.write("\tlw $t0, "+str(addr[4])+"\n")
                file.write("\tsw $t0, "+str(offset)+"($s7)"+"\n")
            else:
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

            if r_addr[3]:
                file.write("\tlw $t1, "+str(addr[4])+"\n")
            else:
                if r_addr[1] == "addr":
                    file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd $t1, $zero, "+str(r_addr[0])+"\n")

            file.write("\tsw $t1, ($t0)"+"\n")

        elif op == "=" :
            l_addr = getAddr(line[1])
            l_offset = l_addr[0]

            r1_addr = getAddr(line[2])

            if r1_addr[3]:
                file.write("\tlw $t0, "+str(r1_addr[4])+"\n")
            else:
                if r1_addr[1] == "addr":
                    file.write("\tlw $t0, "+str(param_size - r1_addr[0] + reg_size - r1_addr[2])+"($s7)"+"\n")
                else:
                    print("[WriteCode]IN =")
                    print(r1_addr[0])
                    file.write("\tadd $t0, $zero, "+str(r1_addr[0])+"\n")

            if l_addr[3]:
                file.write("\tsw $t0, "+str(l_addr[4])+"\n")
            else:
                file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")

        # binary operators
        elif op == "+" or op == "-" or op == "*" or op == "/" or op == "%":

            l_addr = getAddr(line[1])
            l_offset = l_addr[0]
            r1_addr = getAddr(line[2])
            r2_addr = getAddr(line[3])

            if r1_addr[3]:
                file.write("\tlw $t0, "+str(r1_addr[4])+"\n")

            else:
                if r1_addr[1] == "addr":
                    file.write("\tlw $t0, "+str(param_size - r1_addr[0] + reg_size - r1_addr[2])+"($s7)"+"\n")
                else:
                    print("[WriteCode]")
                    print(r1_addr[0])
                    print(line)
                    file.write("\tadd $t0, $zero, "+str(r1_addr[0])+"\n")

            if r2_addr[3]:
                file.write("\tlw $t1, "+str(r2_addr[4])+"\n")

            else:
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

            print("[OP+]")
            print(l_offset)
            print(param_size)
            if l_addr[3]:
                file.write("\tsw $t0, "+str(l_addr[4])+"\n")
            else:
                file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")

        # relational operators
        elif op == "if<" or op == 'if<=' or op == 'if>' or op == 'if>=' or op == 'if==' or op == 'if!=':
            l_addr = getAddr(line[1])
            r_addr = getAddr(line[2])
            l_offset = l_addr[0]

            if l_addr[3]:
                file.write("\tlw $t0, "+str(l_addr[3])+"\n")
            else:
                if l_addr[1] == "addr":
                    file.write("\tlw $t0, "+str(param_size - l_addr[0] + reg_size - l_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd $t0, $zero, "+l_addr[0]+"\n")
            if r_addr[3]:
                file.write("\tlw $t1, "+str(r_addr[3])+"\n")
            else:
                if r_addr[1] == "addr":
                    file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd $t1, $zero, "+str(r_addr[0])+"\n")
            # L attached to all the labels
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

        # Unary operators
        elif op == "~":
            l_addr = getAddr(line[1])
            l_offset = l_addr[0]
            r_addr = getAddr(line[2])
            if r_addr[1] == "addr":
                file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
            else:
                file.write("\tadd $t0, $zero, "+r_addr[0]+"\n")
            file.write("\tnot $t0, $t1"+"\n")
            file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")

        elif op == "array_access":
            r_addr = getAddr(line[2])
            l_addr = getAddr(line[1])
            r_name = line[2].global_name 
            print("{array_access}")
            print(r_name)

            if r_addr[1] == "addr":
                file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
            else:
                file.write("\tadd $t1, $zero, "+r_addr[0]+"\n")
            
            file.write("\tlw $t0, "+str(r_name)+"($t1)"+"\n")
            file.write("\tsw $t0, "+str(param_size - l_addr[0] + reg_size - l_addr[2])+"($s7)"+"\n")

        elif op == "MOVOFFSET":
            l_name = line[1].global_name
            r_addr = getAddr(line[2])
            l_addr = getAddr(line[1])
            print("[MOVOFFSET]")
            print(l_name)
            
            if r_addr[1] == "addr":
                file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
            else:
                file.write("\tadd $t1, $zero, "+str(r_addr[0])+"\n")

            file.write("\tlw $t0, "+str(param_size - l_addr[0] + reg_size - l_addr[2])+"($s7)"+"\n")

            file.write("\tsw $t1, "+str(l_name)+"($t0)"+"\n")

        elif op == "deref":
            l_addr = getAddr(line[1])
            l_offset = l_addr[0]
            r_addr = getAddr(line[2])
            file.write("\tlw $t1, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"($s7)"+"\n")
            file.write("\tlw $t0, ($t1)"+"\n")
            if l_addr[3]:
                file.write("\tsw $t0, "+str(l_addr[4])+"\n")
            else:
                file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")

        elif op == "&":
            l_addr = getAddr(line[1])
            l_offset = l_addr[0]
            r_addr = getAddr(line[2])
            if line[1].isArrayRef:
                t_elem = line[1].array_pointer
                t_addr = getAddr(t_elem)
                file.write("\tlw $t0, "+str(param_size - t_addr[0] + reg_size - t_addr[2]))
            else: 
                file.write("\tadd $t0, $s7, "+str(param_size - r_addr[0] + reg_size - r_addr[2])+"\n")

            if l_addr[3]:
                file.write("\tsw $t0, "+str(l_addr[4])+"\n")
            else:
                file.write("\tsw $t0, "+str(param_size - l_offset + reg_size - l_addr[2])+"($s7)"+"\n")


        elif op == "if":

            l_addr = getAddr(line[1])
            if l_addr[3]:
                file.write("\tlw $t0, "+str(l_addr[4])+"\n")
            else:
                if l_addr[1] == "addr":
                    file.write("\tlw $t0, "+str(param_size - l_addr[0] + reg_size - l_addr[2])+"($s7)"+"\n")
                else:
                    file.write("\tadd $t0, $zero, "+str(l_addr[0])+"\n")
            branchTo = "L"+str(line[-1])
            file.write("\tbne $t0, $zero " + branchTo+"\n")

        elif op == "goto":

            branchTo = "L"+str(line[-1])
            file.write("\tb " + branchTo+"\n")
            print("[goto]")
            print(line)
            print(branchTo)
