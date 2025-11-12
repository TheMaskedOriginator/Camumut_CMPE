#LIST

fruitsA = ["apple", "apple", "banana", "grapes", "grapes", "grapes", "orange"]
print(fruitsA)
print(fruitsA[3])
print(fruitsA.count("grapes"))

isthere1 = "dragon fruit" in fruitsA
isthere2 = "apple" in fruitsA
print(isthere1)
print(isthere2)

fruitsA.append("watermelon")
print(fruitsA)

fruitsA.insert(4, "dragon fruit")
print(fruitsA)


#len = LENGTH
print(len(fruitsA))


#Count = counts the number of the character
print(fruitsA.count("apple"))
print(fruitsA.count("orange"))


#Remove = removes the first match value
fruitsA.remove("watermelon")
print(fruitsA)


#
print(fruitsA.index("grapes"))
fruitsA[1] = "pomegranate"
print(fruitsA)


#Create = (append) (insert)
#Delete = (remove) (clear)
#Read = (view)




#jjjhhhhhhhhhhhhhhhuuiujjjjjjjj