import sys

from c_lexer import CLexer

def error_func(err_msg, line, col):
    print("Got an error: {} \n line: {} col: {} ".format(err_msg, line, col))

def look_up_func(name):
    return False;

def on_lbrace_func():
    pass

def on_rbrace_func():
    pass



lexer = CLexer(error_func, on_lbrace_func, on_rbrace_func, look_up_func)
lexer.build()

if (len(sys.argv) > 1):
    for i in range(1,len(sys.argv)):
        file = open(sys.argv[i])
        inp = file.read();
        lexer.input(inp)
        while True:
            tok = lexer.token();
            if not tok : break;
            print(tok)
else:
    while True:
        inp = raw_input(">")
        lexer.input(inp)
        while True:
            tok = lexer.token();
            if not tok : break;
            print(tok)
