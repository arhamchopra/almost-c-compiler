import c_ast
from parse_error import *

priority = {
	'char' : 1, 
	'short' : 2, 
	'int' :  3, 
	'long' : 4, 
	'float' : 5, 
	'double' : 6, 
	'signed' : 0, 
	'unsigned' : 0, 
	'void' : -1,
	}

def group(var):
	if var == 'char' or var ==  'short' or var ==  'int' or var ==  'long':
		return 'uptoInt'
	elif var == 'float' or var == 'double':
		return 'float'
	elif var == 'signed':
		return 'signed'
	elif var == 'unsigned':
		return 'unsigned' 
	elif var == 'void':
		return 'void'
	elif var == 'ptr':
		return 'ptr'
	elif var == 'array':
		return 'array'

def isPointer_Array(type):
	if isinstance(type, c_ast.PtrDecl):
		return 'ptr'

	elif isinstance(type,c_ast.ArrayDecl):
		return 'array'

	else:
		return None

def depth(ptr):
	if isinstance(ptr, c_ast.PtrDecl) or isinstance(ptr, c_ast.ArrayDecl):
		return depth(ptr.type) + 1

	else:
		return 0

def get_type(entry):
	print("Starting get_type")
	if isinstance(entry, basestring):
	    return (entry, None)

	elif isinstance(entry, c_ast.PtrDecl):
		return ('ptr', depth(entry))
	
	elif isinstance(entry, c_ast.ArrayDecl):
		return ('array', depth(entry))

	print("Not Array")

	while not isinstance(entry, c_ast.Constant) and not isinstance(entry, c_ast.IdentifierType):
		print("ENTRY "+str(entry))
	entry = entry.type

	if isinstance(entry, c_ast.IdentifierType):
		entry = (entry.type)[0]
	else:
		entry =entry.type

	print("return of get_type "+str(entry))
	return (entry, None)


def bin_operator(op,left, right):
	print("Starting Bin_operator")
	typel = get_type(left)
	print("typel " + str(typel))
	typer = get_type(right)
	print("typer " + str(typer))
	groupl = group(typel[0])
	print("groupl " + str(groupl))
	groupr = group(typer[0])
	print("groupr " + str(groupr))

	# if groupl == :
	# 	if(priority[typel[0]] == priority[typer[0]]):
	# 		return (None, None)
	# 	elif priority[typel[0]] < priority[typer[0]]:
	# 		return ('right', None)
	# 	else:
	# 		return (None, 'left')
	# else:
	# 	return 'error'

	if op == '+':
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (right, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)

		elif ((groupl == 'ptr' or groupl == 'array') and (groupr == 'uptoInt')):
			return (left, None, None)

		elif ((groupr == 'ptr' or groupr == 'array') and (groupl == 'uptoInt')):
			return (right, None, None)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
		
		else:
			adderror("wrong arguements passed to binary operator +")
			return('int', None, None)

	elif op == '-':
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (right, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)

		elif ((groupl == 'ptr' or groupl == 'array') and (groupr == 'ptr' or groupr == 'array')):
			if typel[1] == typer[1]:
				t = c_ast.IdentifierType(['int'])
				return (t, None, None)
			else:
				adderror("wrong arguements passed to binary operator -")
				return('int', None, None)


		elif ((groupl == 'ptr' or groupl == 'array') and (groupr == 'uptoInt')):
			return (left, None, None)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
		else:
			adderror("wrong arguements passed to binary operator -")
			return('int', None, None)

# club
	elif op == '*' or op ==  '/':
		print("arguements passed to binary operator " + op)
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			print("Both Ints")
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (right, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
		
		else:
			#  print("wrong arguements passed to binary operator " + op)
			adderror("wrong arguements passed to binary operator " + op)
			return('int', None, None)


	elif op == '|' or op == '&' or op == '^' or op == '<<' or op == '>>' or op == '%':
		if groupl == 'uptoInt' and groupr == 'uptoInt':
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (right, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
		
		else:
			#  print("wrong arguements passed to binary operator " + op)
			adderror("wrong arguements passed to binary operator " + op)
			return('int', None, None)

	elif op == '||' or op == '&&':
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			t = c_ast.IdentifierType(['int'])
			return (t, None, None)

		elif ((groupl == 'ptr' or groupl == 'array') and (groupr == 'uptoInt')):
			t = c_ast.IdentifierType(['int'])
			return (t, None, None)

		elif ((groupr == 'ptr' or groupr == 'array') and (groupl == 'uptoInt')):
			t = c_ast.IdentifierType(['int'])
			return (t, None, None)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			t = c_ast.IdentifierType(['int'])
			return (t, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			t = c_ast.IdentifierType(['int'])
			return (t, None, None)

		elif ((groupl == 'ptr' or groupl == 'array') and (groupr == 'ptr' or groupr == 'array')):
			t = c_ast.IdentifierType(['int'])
			return (t, None, None)
		else:
			adderror("wrong arguements passed to binary operator" + op)
			return('int', None, None)

#end

# pointers can use this function 
	elif op == '<' or '>' or op == '<=' or op == '>=' or op == '==' or op =='!=':
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (right, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
		
		elif ((groupl == 'ptr' or groupl == 'array') and (groupr == 'ptr' or groupr == 'array')):
			if typel[1] == typer[1]:
				t = c_ast.IdentifierType(['int'])
				return (t, None, None)
		else:
			adderror("wrong arguements passed to binary operator +")
			return('int', None, None)

# End
	    # Assignment operators
	elif op == '=':
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			else:
				return (left, None, left)

		elif ((groupl == 'ptr' ) and (groupr == 'ptr' or groupr == 'array')):
			if typel[1] == typer[1]:
				return (left, None, None)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
		else:
			adderror("wrong arguements passed to binary operator" + op)

	elif op == '*=' or op == '/=':
		if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (left, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)
			else:
				return (left, None, left)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
		else:
			adderror("wrong arguements passed to binary operator" + op)



	elif op == '+=':
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (left, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)

		elif ((groupl == 'ptr') and (groupr == 'uptoInt')):
			return (left, None, None)


		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
		
		else:
			adderror("wrong arguements passed to binary operator +")

	elif op == '-=':
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (left, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)

		elif ((groupl == 'ptr') and (groupr == 'uptoInt')):
			return (left, None, None)


		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)


	elif op == '%=' or op  == '<<=' or op == '>>=' or op == '&=' or op == '|=' or op == ' ^=':
		if (groupl == 'uptoInt' ) and (groupr == 'uptoInt'):
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (left, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
	


	#     Increment/decrement
def unary_operator(oper, key):
	print("Starting unary_operator")
	typeKey = get_type(left)
	print("typeKey " + str(typel))
	groupl = group(typeKey[0])

	if op == '++' or op == '--' or op == '!' or op == '~':
		return key

	elif op == '*':
		assert key.type is not None
		return key.type

	elif op == '&':
		t = c_ast.PtrDecl([], key)
		return t
	#     # ->
	# elif op == '->':




	#     # Delimeters
	# elif op == :

	# elif op == ')':

	# elif op == :

	# elif op == ']':

	# elif op == :

	# elif op == '.':

	# elif op == ';':

	# elif op == ':':

	# elif op == '...':
