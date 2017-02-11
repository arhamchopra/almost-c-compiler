from c_parser import *

last = 1
fname = "ParseTree.ps"

while sys.argv[last].startswith("-"):
	print(sys.argv[last])
	if sys.argv[last] == "-v":
		print("Compiler version 0.0.7 made by Chapu Chopra\n")
		sys.exit(0)
	elif sys.argv[last] == "-help":
		sys.exit(0)
	elif sys.argv[last] == "-o":
		fname = sys.argv[2]
		last+=2
		sys.exit(0)
	else :
		print("invalid flag\n")
		sys.exit(0)

inFile = sys.argv[last]
with open(inFile, 'r') as inp:
	parser = CParser(lex_optimize=False, yacc_debug=False, yacc_optimize=False)
	text = inp.read()
	parser.parse(text)
	saveGraph(fname)
