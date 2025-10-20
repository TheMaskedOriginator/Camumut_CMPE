# str functions

strFullName = "Kirk Claret Sistona Camumut"

intLength = len(strFullName)

print(intLength)
print(strFullName[0])
print(strFullName[11])
print(strFullName[15])
print(strFullName[25])
print(strFullName[intLength - 3])

strInputFromUser = "Alisa Lei Elia Corpez"

strFullName = strInputFromUser
print(strFullName)
intLength = len(strFullName)
print(intLength)

# Passing of Value; One value to another; Input Process Output

strFullName = "Kirk Claret Sistona Camumut"

# Upper
strNewValue = strFullName.upper()
print(strNewValue)

# Count
strNewValue = strFullName.count("u")
print(strNewValue)

# Split - all
strNewValue = strFullName.split(" ")
print(strNewValue)

# Split - one character
strNewValue = strFullName.split("m")
print(strNewValue)

# Replace
strNewValue = strFullName.replace("Kirk Claret ", "Jose Protacio Rizal Mercado ")
print(strNewValue)

# Join
strFirstName1 = "Kirk"
strFirstName2 = "Claret"
strMiddleName = "Sistona"
strLastName = "Camumut"
strFullName = " ♡ ♡ ".join([strFirstName1, strFirstName2, strMiddleName, strLastName])
print(strFullName)

# isnumeric
strNewValue =  strFullName.isnumeric()
print(strNewValue)

# Index - gives the index number of the string; mode; return the lowest index available
# Kirk ♡ ♡ Claret ♡ ♡ Sistona ♡ ♡ Camumut
strNewValue =  strFullName.index("C")
print(strNewValue)

strNewValue =  strFullName.index("C", 10, 38)
print(strNewValue)

# Substring
strNewValue =  strFullName[9:27]
print(strNewValue)

# If the code contains the character
print("Kirk" in strFullName)

# RegEx - Sample Trial (Small/Short Introduction)
strInput = "123Ohayo321"
print(strInput)
print(strInput.replace("Ohayo", "Hello"))

newString = ""
for char in strInput:
    if not char.isnumeric():
        newString = newString + char

print(newString)


strInput = "1823748I628737048208432 8948L93223O32763524283479267V803724829E041 043875734885Y0984O983748628478926343289U"

newString = ""
for char in strInput:
    if not char.isnumeric():
        newString = newString + char

print(newString)

# Comment: Try debugging this! Its cool FR FR

# Numerical integer (-9, 0, 6)
# Float (23.09894787)
# Complex Number (sqrt. -4, 4 + i35)
# i = ampere; j = imaginary

import math
# Mathematical Operator

myIntegerA = 67
myIntegerB = 99
myIntegerC = 90
myFloatA = 20.25
myFloatB = 02.07
myComplexA = 36 + 8j
myComplexB = 55 - 18j

# +, -, /, *, **(exponent)
sum = myIntegerA + myFloatB
print(sum)

difference = myIntegerB - myFloatA
print(difference)

product = myIntegerA * myIntegerB
print(product)

productComplex = myComplexA * myComplexB
print(productComplex)

quotient = myIntegerA / myFloatB
print(quotient) #Repeating

RoundedQuotient = round(quotient, 2)
print(RoundedQuotient)

result =  2 ** 6
print(result)

# modulu -
remainder = myIntegerA % myFloatB
print(remainder)

kurtAngle = math.cos(1)
print(kurtAngle)

kurtAngle2 = math.degrees(math.cos(1))
print(kurtAngle2)

print(5*4*3*2*1)
print(math.factorial(5))

print(math.cos(math.degrees(90)))

cos_90_deg = math.cos(math.radians(90))
print(cos_90_deg)

isPresent = False #boolean
isExist = True #boolean

isAvailable = "True" #string

isValid = 1 #integer
isOkay = 0 #integer

isNumeric = False
myChar = "5"

isNumeric = myChar.isnumeric()
strIsNumeric = str(myChar.isnumeric())
print([isNumeric])
print([strIsNumeric])

# AND, OR, NOT ------------- EXOR, NOR, NAND
# in, is, not, in, is not
# ==, >=, >, <=, <, !=(not equal to)

# Comparison Operator
a = 4
b = 5
isEqual = (a == b)
print(isEqual)
isLessThan = (a <= b)
print(isLessThan)
answer = (a != b)
print(answer)


# String - enclosed in a "..."
# boolean - vice versa;  true or False answers

# Membership and Identity Operator - included or not
# in, not in, is, is not

isIn = (5 in [25, 45, 23, 12, 5, 27])
print(isIn)
isIn = (5 in [25, 45, 23, 12, 27])
print(isIn)

isIs = ("Ohayo" is "Ohayo")
print(isIs)
isIs = ("Ohayo" is "Hello")
print(isIs)

isGutom = ("gutom" in "Sir gutom na po ako AHHAHA")
print(isGutom)
isJoke = ("Joke" in "Joke lang sir, ehhehe")
print(isJoke)

isOkay = (5 in [25, 45, 23, 12, 5, 27]) and (5 in [25, 45, 23, 12, 27])
print(isOkay)

isOkay = (5 in [25, 45, 23, 12, 5, 27]) or (5 in [25, 45, 23, 12, 27])
print(isOkay)

# Logical Operator


# String Methods
# IDE gives string/code suggestions
# Hover the cursor to the string codes to check their functions
# List - 2 or more splits
# Mean = average of the numbers
# Median = in the middle
# Mode = number that occurs frequently

#MatLab
#Logic.ly