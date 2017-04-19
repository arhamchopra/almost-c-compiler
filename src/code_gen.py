import re

import symbol_table
import c_ast
from symbol_table import getCST, getSize

# TODO In this file 


code_list = []

def emit(key, op, var_tuple):
    print("In Emit")
    print(key, op, var_tuple)
    CST = getCST()
    #  if len(var_tuple) == 3 and not isinstance(var_tuple[2], tuple):
    #      print("HAGGA 1")
    #      temp = CST.provideTemp(var_tuple[0])
    #
    #  if not isinstance(var_tuple[1], tuple):
    #      print("HAGGA HAGGA HAGGA HAGGAPA")
    #      temp = CST.provideTemp(var_tuple[0])
        
    #  print(CST.Print())
    if key == "BinaryOp":
        assert len(var_tuple) == 3
        # Have to separate the operator based on the true list and false list
        # -,+,*,/,^,&,|,~,<<,>>,
        if re.match(r"\-|\+|\*|\/|<=|>=|==|!=|\|\||\&\&|\||\&|\^|<|>|!", op) or op == "<<" or op == ">>":
            print("In BinaryOp"+op)
            temp = CST.provideTemp(var_tuple[0])
            code_list.append((op, temp, var_tuple[1], var_tuple[2]))
            
        elif op == "%":
            temp1 = CST.provideTemp(var_tuple[0])
            temp2 = CST.provideTemp(var_tuple[0])
            temp3 = CST.provideTemp(var_tuple[0])
            code_list.append(("/", temp1, var_tuple[1], var_tuple[2]))
            code_list.append(("*", temp2, temp1, var_tuple[2]))
            code_list.append(("-", temp3, var_tuple[1], temp2))
            temp = temp3

    elif key == "Cast":
        assert len(var_tuple) == 3
        temp = CST.provideTemp(var_tuple[0])
        code_list.append(("Cast", temp, var_tuple[0], var_tuple[1]))


    elif key == "UnaryOp":
        assert len(var_tuple) == 3
        if op == "&":
            temp = CST.provideTemp(var_tuple[0])
            code_list.append(("addr", temp, var_tuple[1], None))
                
        elif op == "*":
            temp = CST.provideTemp(var_tuple[0])
            code_list.append(("deref", temp, var_tuple[1], None))
        
        elif op == "+":
            temp = var_tuple[1]
        
        elif op == "-":
            temp = CST.provideTemp(var_tuple[0])
            code_list.append(("-", temp, 0, var_tuple[1]))

        elif op == "~":
            temp = CST.provideTemp(var_tuple[0])
            code_list.append(("-", temp, -1, var_tuple[1]))

        #  [TODO]
        elif op == "!":
            temp = CST.provideTemp(var_tuple[0])
            code_list.append(("-", temp, -1, var_tuple[1]))

        elif op == "++":
            temp = CST.provideTemp(var_tuple[0])
            code_list.append(("+", temp, var_tuple[1], 1 ))
            code_list.append(("=", var_tuple[1], temp, None))

        elif op == "--":
            temp = CST.provideTemp(var_tuple[0])
            code_list.append(("-", temp, var_tuple[1], 1 ))
            code_list.append(("=", var_tuple[1], temp, None))

        elif op == "p++":
            temp1 = CST.provideTemp(var_tuple[0])
            temp2 = CST.provideTemp(var_tuple[0])
            code_list.append(("=", temp2, var_tuple[1], None ))
            code_list.append(("+", temp1, var_tuple[1], 1 ))
            code_list.append(("=", var_tuple[1], temp1, None))
            temp = temp2
        
        elif op == "p--":
            temp1 = CST.provideTemp(var_tuple[0])
            temp2 = CST.provideTemp(var_tuple[0])
            code_list.append(("=", temp2, var_tuple[1], None ))
            code_list.append(("-", temp1, var_tuple[1], 1 ))
            code_list.append(("=", var_tuple[1], temp1, None))
            temp = temp2           

    elif key == "Assignment":
        print("[Assignment]IN Assignemnt")
        if op == "=":
            temp = var_tuple[2]
            code_list.append(("=", var_tuple[1], temp, None))
        else:
            op_equal = op[-1]
            op_exp = op[:-1]
            temp1 = CST.provideTemp(var_tuple[0])
            code_list.append((op_exp, temp1, var_tuple[1], var_tuple[2]))
            code_list.append((op_equal, var_tuple[1], temp1))
            temp = temp1 

    elif key == "ArrayRef":
        print("In Array Ref")
        temp1 = CST.provideTemp(c_ast.IdentifierType(['int']))
        type = var_tuple[1][2].getElementAtIndex(var_tuple[1][1])[1]
        size = getSize(var_tuple[0])
        code_list.append(("*", temp1, var_tuple[2], size))
        
        temp2 = CST.provideTemp(type)
        code_list.append(("+", temp2, temp1, var_tuple[1]))

        temp3 = CST.provideTemp(var_tuple[0])
        code_list.append(("deref", temp3, temp2, None))
        temp = temp3
    elif key == "FuncCall":
        print("[emit]FuncCall")
        temp1 = CST.provideTemp(var_tuple[0])
        for var in var_tuple[2]:
            print("[emit]Pushing the tuple "+str(var))
            code_list.append(('push', None, var.refer, None))
        #[TODO] Check if the length of function list should be passed or not
        code_list.append(('call',temp1, var_tuple[1],len(var_tuple[2])))

        #[TODO] Add code for activation records here
        temp = temp1
    elif key == "FuncDef":
        code_list.append(("begin", None, var_tuple))
        temp = None


        
    
    return temp

def PrintCode():
    print("We are now printing the 3AC Code ------------------------------------------------")
    for i in code_list:
        print(i)

def getReference(name):
    print("In getReference")
    CST = getCST()
    entry = CST.lookupFullScope(name)
    if(entry[-1] == "ST"):
        return entry[5] 
    else:
        return None        

