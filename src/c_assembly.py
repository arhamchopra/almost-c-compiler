#  This file will generate the asm code that will run

import c_ast
from symbol_table import *

code_list = c_ast.getCode()

#  def fix_
#

def getAddr(obj):
    if isinstance(obj, c_ast.TAC):
        refer = obj.refer
        if type(refer) == tuple:
            refer = getSTEntry(refer)
            print("[getAddr]")
            print(refer)
            offset = -1*refer[2] 
            return (offset, "addr")
        else:
            return (refer, "const")
    else:
        return (obj, "const")

def writeCode():
    file = open('assembly.asm', 'w')
    file.write(".data"+"\n")
    file.write(".text"+"\n")

    for line in code_list:
        op = line[0]
        #  print(line)
        if op == "begin":
            #  print(line)
            name = getSTEntry(line[2].refer)[0]
            #  print(name)
            file.write(name+":"+"\n")
        elif op == "=" :
            l_addr = getAddr(line[1])
            #  l_refer = getSTEntry(line[1].refer)
            #  l_offset = -1*refer[2]
            l_offset = l_addr[0]

            r1_addr = getAddr(line[2])
            r2_addr = getAddr(line[3])
            if r1_addr[1] == "addr":
                file.write("\tlw $t0, "+str(r1_addr[0])+"($sp)"+"\n")
            else:
                file.write("\tadd $t0, $zero, "+str(r1_addr[0])+"\n")

            file.write("\tsw $t0, "+str(l_offset)+"($sp)"+"\n")

        elif op == "+" :
            #  print(line)
            #  Assuming only constants in operands

            l_addr = getAddr(line[1])
            #  l_refer = getSTEntry(line[1].refer)
            #  l_offset = -1*refer[2]
            l_offset = l_addr[0]

            r1_addr = getAddr(line[2])
            r2_addr = getAddr(line[3])

            if r1_addr[1] == "addr":
                file.write("\tlw $t0, "+str(r1_addr[0])+"($sp)"+"\n")
            else:
                file.write("\tadd $t0, $zero, "+r1_addr[0]+"\n")

            if r2_addr[1] == "addr":
                file.write("\tlw $t1, "+str(r2_addr[0])+"($sp)"+"\n")
            else:
                file.write("\tadd $t1, $zero, "+r2_addr[0]+"\n")

            file.write("\tadd $t0, $t0, $t1"+"\n")
            file.write("\tsw $t0, "+str(l_offset)+"($sp)"+"\n")


    
    file.write("\tli $v0, 1"+"\n")
    file.write("\tlw $t1, 0($sp)"+"\n")
    file.write("\tadd $a0, $zero, $t1"+"\n")
    file.write("\tsyscall"+"\n")

    file.write("\tli $v0, 10"+"\n")
    file.write("\tsyscall"+"\n")


#  For push

            #  file.write("\tadd $t1, $zero, "+str(line[2])+"\n")
            #  file.write("\tadd $t2, $zero, "+str(line[3])+"\n")
            #  file.write("\tadd $sp, $sp, -4"+"\n")
            #  file.write("\tsw $t3, 0($sp)"+"\n")

