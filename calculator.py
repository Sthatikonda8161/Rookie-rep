print()
print("Welcome to 'XYZ Calculator'")
print()


def addCal(a, b):
  print(a+b)

def subCal(c, d):
  print(c-d)

def mulCal(e, f):
  print(e*f)

def divCal(g, h):
  print(g/h)

Input1 = int(input('Enter the First number : '))
Input2 = int(input('Enter the Second number : '))

choice = input('Enter the calculation function: ')

if(choice == '1'):
 addCal(Input1, Input2)
elif(choice == '2'):
 subCal(Input1, Input2)
elif(choice == '3'):
 mulCal(Input1, Input2)
elif(choice == '4'): 
 divCal(Input1, Input2)
else:
  print("Entry miss matched please try again")

