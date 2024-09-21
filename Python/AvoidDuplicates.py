words=[]
while True:
    word = input("Enter a word (blank to stop): ")
    if word == "":
        break
    if word not in words:
        words.append(word)
print("\nUnique words in the order entered:")
for word in words:
    print(word)        