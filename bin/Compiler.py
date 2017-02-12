from c_parser import *
from parse_tree import *

last = 1
fname = "ParseTree.png"

while last<len(sys.argv) and sys.argv[last].startswith("-"):
	print(sys.argv[last])
	if sys.argv[last] == "-v":
		print("Compiler version 0.0.7 made by Chapu Chopra\n")
		sys.exit(0)
	elif sys.argv[last] == "-h" or sys.argv[last] == "--help":
                print("THIS IS OUR HELP")
		sys.exit(0)
	elif sys.argv[last] == "-o" and sys.argv[last+1] != "" :
	        fname = sys.argv[last+1]
	        last+=1
	else :
		print("invalid flag\n")
		sys.exit(0)
	last+=1

if last<len(sys.argv):
    inFile = sys.argv[last]
    print(inFile)
    with open(inFile, 'r') as inp:
            parser = CParser(lex_optimize=False, yacc_debug=True, yacc_optimize=False)
            text = inp.read()
            print(text)
            parser.ParseInput(text, fname)
