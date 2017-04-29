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


user_debug = False 
    
def printDebug(s):
    if user_debug:
        print(s)

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
		(d,t) = depth(ptr.type)
		return(d+1,t)

	else:
		if isinstance(ptr, c_ast.TypeDecl):
			return (0,ptr.type.names[0])
		elif  isinstance(ptr, c_ast.IdentifierType):
			return (0,ptr.names[0])

def get_type(entry):
	printDebug("Starting get_type")
	if isinstance(entry, basestring):
	    return (entry, None)

	elif isinstance(entry, c_ast.PtrDecl):
		return ('ptr', depth(entry))
	
	elif isinstance(entry, c_ast.ArrayDecl):
		return ('array', depth(entry))
# Not an Array or Pointer
	printDebug("ENTRY "+str(entry))
	while not isinstance(entry, c_ast.Constant) and not isinstance(entry, c_ast.IdentifierType):
	        entry = entry.type

	if isinstance(entry, c_ast.IdentifierType):
		entry = (entry.type)[0]
	else:
		entry =entry.type

	printDebug("return of get_type "+str(entry))
	return (entry, None)

def valid_sub(ptr):
	if isinstance(ptr, c_ast.PtrDecl):
		return valid_sub(ptr.type)
	elif isinstance(ptr, c_ast.ArrayDecl):
		if not isinstance(ptr.type, c_ast.ArrayDecl):
			return True
		else:
			return False
	elif isinstance(ptr, c_ast.TypeDecl):
		return  True


def bin_operator(op, left, right):
        print("[bin_operator] Left:"+str(left)+" Right:"+str(right))
	printDebug("Starting Bin_operator")
	typel = get_type(left)
	printDebug("typel " + str(typel))
	typer = get_type(right)
	printDebug("typer " + str(typer))
	groupl = group(typel[0])
	printDebug("groupl " + str(groupl))
	groupr = group(typer[0])
	printDebug("groupr " + str(groupr))

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
			return ("error",typel[0],typer[0] ) 

			# add function to print the complete pointer 
		# if (groupl == 'float') and  (groupr == 'signed' or groupr == 'unsigned'):
			
		# 	if groupl == d
			# adderror("wrong arguements" + "passed to binary operator" + op )

	elif op == '-':
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			if priority[typer[0]] == priority[typel[0]]:
				return (left, None, None)
			elif priority[typer[0]] > priority[typel[0]]:
				return (right, right, None)
			elif priority[typer[0]] < priority[typel[0]]:
				return (left, None, left)

		elif ((groupl == 'ptr' or groupl == 'array') and (groupr == 'ptr' or groupr == 'array')):
			if typel[1] == typer[1] and valid_sub(left) and valid_sub(right):
				t = c_ast.IdentifierType(['int'])
				return (t, None, None)
			else:
				return ("error",typel[0],typer[0] ) 
				# adderror("wrong arguements passed to binary operator -")
				# return('int', None, None)


		elif ((groupl == 'ptr' or groupl == 'array') and (groupr == 'uptoInt')):
			return (left, None, None)

		elif groupl == 'unsigned' and groupr == 'unsigned':
			return (left, None, None)

		elif groupl == 'signed' and groupr == 'signed':
			return (left, None, None)
		else:
			return ("error",typel[0],typer[0] ) 

			# adderror("wrong arguements" "and" "passed to binary operator" + op)
			# return('int', None, None)

# club
	elif op == '*' or op ==  '/':
		printDebug("arguements passed to binary operator " + op)
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):
			printDebug("Both Ints")
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
			return ("error",typel[0],typer[0] ) 

			# adderror("wrong arguements passed to binary operator " + op)
			# return('int', None, None)


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
			return ("error",typel[0],typer[0] ) 

			# adderror("wrong arguements passed to binary operator " + op)
			# return('int', None, None)

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
			return ("error",typel[0],typer[0] ) 

			# adderror("wrong arguements passed to binary operator" + op)
			# return('int', None, None)

#end

# pointers can use this function 
	elif op == '<' or op == '>' or op == '<=' or op == '>=' or op == '==' or op =='!=':
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
			return ("error",typel[0],typer[0] ) 

			# adderror("wrong arguements passed to binary operator +")
			# return('int', None, None)

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
			return ("error",typel[0],typer[0] ) 
			# adderror("wrong arguements passed to binary operator" + op)

	elif op == '*=' or op == '/=':
		if (groupl == 'uptoInt' or groupl == 'float') and (groupr == 'uptoInt' or groupr == 'float'):

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
			return ("error",typel[0],typer[0] ) 
			# adderror("wrong arguements passed to binary operator" + op)



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
			return ("error",typel[0],typer[0] ) 
			# adderror("wrong arguements passed to binary operator +")

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

		else:
			return ("error",typel[0],typer[0] ) 



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
		else:
			return ("error",typel[0],typer[0]) 



	#     Increment/decrement
def uni_operator(op, key):
	printDebug("Starting unary_operator")
	typeKey = get_type(key)
	printDebug("typeKey " + str(typeKey))
	groupKey = group(typeKey[0])
	printDebug("groupKey" + str(groupKey))

	if op == '++' or op == '--' or op == '~':
		if groupKey == "uptoInt":
			return key
		else:
			return 'error'
			# adderror("Incorrect type in unary_operator "+oper)
			# return c_ast.IdentifierType(['int'])

	elif op == '!':
		return c_ast.IdentifierType(['int'])

	elif op == '*':
		if isinstance(key, c_ast.PtrDecl) or isinstance(key, c_ast.ArrayDecl):
			return key.type
		else:
			return 'error'
	elif op == '&':
		t = c_ast.PtrDecl([], key)
		return t
        elif op == '-' or op == '+':
                return key

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
