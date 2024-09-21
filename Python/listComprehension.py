import random
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist = [x for x in fruits if "a" in x]
#newlist = [x.upper() for x in fruits]
newlist = [x if x!='banana' else 'orange' for x in fruits]
print(newlist)
print([i**2 for i in range(10)])
li=[random.choice("abcdefgh") for i in range(3)]
print(li)