We have obtained our Grammar from eliben/pycparser

Changes done:
1) We added a file for Symbol Table Class. We inserted the different function in this class at the required places in the c_parser.py file

2) We changed the show function of a node in c_ast so that it would start printing the ast in a png. We c_ast code to not print certain nodes and print certain other nodes in a different fashion. For this, we had to change the declaration of some classes to incorporate certain fields that were required.

3) We added a file for implementing type checking. The file took as input different operators and produced a tuple containing the type cast of each operand with the type check completed. We also handled pointers and arrays in this file such that only correct expression would not result in an error. We could not do the type checking and casting for function declaration and definitions.

4) We could only finish error handling for expression where there was a type check error and we also handled error for incorrect initialization and use of arrays and pointers

5) We also added code for size determination but this was not working correctly so we commented it out.

6) We also made changes to the code already present in c_parser. We modified _build_declarations to allow type checking during initialization. We modified _add_identifier to add the variables to the correct Symbol Table. We added a _get_type function to obtain the type of different c_ast objects. We modified the lex_on_lbrace_function and lex_on_rbrace_function to changed the Symbol Table scopes. We also changed the grammar at certain points to allow easy type checking
