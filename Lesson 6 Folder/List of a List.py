# List of a List example

fruitsA = ["apple", "apple", "banana", "grapes", "grapes", "grapes", "orange"]
fruitsB = ["pomegranate", "pomegranate", "mango", "mango", "watermelon", "strawberry", "strawberry"]
fruitsC = ["pineapple", "pineapple", "pineapple", "papaya", "papaya", "lychee", "lychee"]

# Different lists
FruitBasket = [fruitsA, fruitsB, fruitsC]
print(FruitBasket)
print(FruitBasket[2])
print(FruitBasket[2][1])

# All subjects in one list
FruitBasket_Uno = fruitsA + fruitsB + fruitsC
print(FruitBasket_Uno)


# + ---> single list
# , ---> list of a list


fruitsA.extend(fruitsB)
fruitsB.extend(fruitsC)
print(fruitsA)


