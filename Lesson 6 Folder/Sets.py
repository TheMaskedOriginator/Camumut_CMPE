# Set = does not allow duplicates; removes duplicates; always not in order

fruitsA = {"apple", "apple", "banana", "grapes", "grapes", "grapes", "orange"}
fruitsB = {"pomegranate", "pomegranate", "mango", "mango", "watermelon", "strawberry", "strawberry"}
print(fruitsA)

fruitsA.add("rambutan")
print(fruitsA)

FRUnion = fruitsA.union(fruitsB)
print(FRUnion)

fruitIntersect = fruitsA.intersection(fruitsB)
print(fruitIntersect)

fruitDiff1 = fruitsA.difference(fruitsB)
print(fruitDiff1)

fruitDiff2 = fruitsB.difference(fruitsA)
print(fruitDiff2)


# Lists of a set

fruitsA = {"apple", "apple", "banana", "grapes", "grapes", "grapes", "orange"}
fruitsB = {"pomegranate", "pomegranate", "mango", "mango", "watermelon", "strawberry", "strawberry"}

fruitbasketList = [fruitsA, fruitsB]
print(fruitbasketList)

