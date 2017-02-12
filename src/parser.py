#!/usr/bin/python    

from c_parser import *
from parse_tree import * 

last = 1
fname = "ParseTree.png"

while last<len(sys.argv) and sys.argv[last].startswith("-"):
	if sys.argv[last] == "-v":
		print("Compiler Version 0.0.1\n")
		sys.exit(0)
	elif sys.argv[last] == "-h" or sys.argv[last] == "--help":
                print("Usage: ./src/parser.py [options] file ")
                print("Options :")
                print("\t -v \t\t Display the version of the compiler")
                print("\t -h \t\t Display usage of the compiler")
                print("\t -o filename(ext. png) \t\t Parse the input file and write output into filename")
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
            parser = CParser(lex_optimize=False, yacc_debug=False , yacc_optimize=False)
            text = inp.read()
            print(text)
            parser.ParseInput(text, fname)
