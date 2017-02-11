from c_parser.py import *

last = 1
fname = "ParseTree.ps"

while argv[last].startswith("-"):
	if argv[last] = "-v":
		print("Compiler version 0.0.7 made by Chapu Chopra\n")
		return
	elif argv[last] = "-help":
		print("please contact customer care for help and support\n")
		return
	elif argv[last] = "-o":
		fname = argv[2]
		last+=2
	else
		print("invalid flag\n")

else:
	inFile = sys.argv[last]