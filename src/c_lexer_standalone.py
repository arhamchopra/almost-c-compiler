from c_lexer import CLexer

def error_func(err_msg, line, col):
    print("Got an error: {} \n line: {} col: {} ".format(err_msg, line, col))

def look_up_func(name):
    return False;

lexer = CLexer(error_func, None, None, look_up_func)
lexer.build()
while True:
    inp = raw_input(">")
    lexer.input(inp)
    while True:
        tok = lexer.token();
        if not tok: break;
        print(tok)
