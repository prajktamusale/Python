thistuple = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple[y]
# print(x)
# y = list(x)
# y.append("orange")
# x = tuple(y)
# y = ("orange",)
# thistuple += y
# print(thistuple)
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)