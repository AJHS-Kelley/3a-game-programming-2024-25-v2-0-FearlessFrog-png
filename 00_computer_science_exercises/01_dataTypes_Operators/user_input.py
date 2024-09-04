# User Input Practice, Tegan Robinson, v0.0

# input() is the built-in function to get information from the KEYBOARD
# BASIC EXAMPLE
variableName = input("Please type a variable name and press enter.\n")
print(variableName) 

# input() saves ALL INPUT DATA TYPES BY DEFULT!!!
# input() saves ALL INPUT DATA TYPES By DEFULT!!!
# input() saves ALL INPUT DATA TYPES BY DEFULT!!!
# input() saves ALL INPUT DATA TYPES BY DEFULT!!!

# INCORRECT, CAUSES A CONCATENATION ERROR.
# MyNumber = input("Please type an INTEGER number and press enter.\n")
## print(myNumber + 5)

# CORRECt -- Use a wraper.
myNumber = int(input("Please type an INTEGER number and press enter.\n"))
print(myNumber + 5)       

# Wrapper Functions
# int() will convert the data to an INTEGER if possible.
newNumber = input("Please type a value and press enrter.\n)")
print(int(newNumber)) # can convert STRING to INTEGER
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can convert INTEGEr to STRING.

# float() will convert the data to a Float if possible.
newNumber = input("Please type a value and press enter.\n")
# print(int(newNumber)) <-- cannot convert FLOAT to INTEGER
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # can conver FLOAT to STRING

# str() will convert the data to a STRONG if possible.
newNumber = 5
print(newNumber + newNumber) # Should print 10
print(str(newNumber + newNumber)) # Should print 55.