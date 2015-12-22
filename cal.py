#Programmer: Ronel B. Llarenas

def add(num1, num2):
	return num1 + num2
 


def sub(num1, num2):
	return num1 - num2
 

def multiply(num1, num2):
	return num1 * num2


def div(num1, num2):
	return num1 / num2

def main():
	operation = input (" ano gusto mo?(+, -, *, /)")

	if(operation != '+' and operation != '-' and operation != '*' and operation != '/'):
		print ("invalid operation! ulol!")

	else:
		var1 = int(input("una mo nga number ibutang!:"))
		var2 = int(input("ikaduwa nga number ibutang!:"))
		if (operation == '+'):
			print (add(var1, var2))

		elif (operation == '-'):
			print (sub(var1, var2))

		elif (operation == '*'):
			print (multiply(var1, var2))

		else: 
			print (div(var1, var2))
main()

main()
main()
main()

