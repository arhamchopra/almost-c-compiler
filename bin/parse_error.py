errors = []

counter = 0
def adderror(err):
	global counter
	counter+=1
	errors.append(err + "\n")

def printerror():
	for i in errors:
		print(i)

def getErrorCount():
	global counter
	return counter

def getErrorMsg():
	return errors