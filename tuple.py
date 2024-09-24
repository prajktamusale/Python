#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple
# thistuple = ("apple",)
# print(type(thistuple))
thistuple = tuple(("apple", "banana", "cherry", "kiwi","melon", "mango"))
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])