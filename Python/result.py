max=0
min=100
num=0
while num!=-1:
    num=int(input("Enter your marks :"))
    if max<num:
        max=num
    if min>=num and num !=-1:
        min=num
print("max",max)
print("min",min)            