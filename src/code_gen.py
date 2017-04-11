import symbol_table
import c_ast
from c_parser import global_CST
from c_parser import global_GST

code_list = []

def emit(key, op, var_tuple):
    if key == "BinaryOp":
        assert len(var_tuple) == 3
        temp = global_CST.provideTemp(var_tuple[0])
        code_list.append(("BinaryOp", temp, var_tuple[1], var_tuple[2]))

    if key == "Cast":
        assert len(var_tuple) == 2
        temp = global_CST.provideTemp(var_tuple[0])
        code_list.append(("Cast", temp, var_tuple[0], var_tuple[1]))

    if key == "UnaryOp":
        assert len(var_tuple) == 3
        if var_tuple[1] == "PlusPlus":
            temp = global_CST.provideTemp(var_tuple[0])
            code_list.append(("BinaryOp", temp, var_tuple[2]))
            

