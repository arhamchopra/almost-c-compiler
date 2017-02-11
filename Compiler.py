from c_parser.py import *

last = 1
fname = "ParseTree.ps"

while argv[last].startswith("-"):
	if argv[last] is "-v":
		print("Compiler version 0.0.7 made by Chapu Chopra\n")
		return
	elif argv[last] is "-help":
		print("please contact customer care for help and support\n")
		return
	elif argv[last] is "-o":
		fname = argv[2]
		last+=2
		return
	else
		print("invalid flag\n")
		return

else:
	inFile = sys.argv[last]
	with open(inFile, 'r') as inp:
        parser = CParser(lex_optimize=False, yacc_debug=False, yacc_optimize=False)
        text = inp.read()
        parser.parse(text)
        saveGraph(fname)
