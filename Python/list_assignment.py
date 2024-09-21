names=[]
while True:
    name = input("Enter a name(or 'End' to finish): ")
    if name == "End" or name == "end":
        break
    names.append(name)
    
half_length=len(names)//2
if len(names)%2 ==1:
    half_length=half_length+1
    
print("First half of the list: ")
print(names[:half_length])    

    
    
    

    

