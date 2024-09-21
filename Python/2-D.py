student=[]
name=input("enter name")
while True:
    temp=[]
    if name == "End":
        break
    temp.append(name)
    for i in range(4):
        marks=int(input("enter marks"))
        temp.append(marks)
    student.append(temp)
    name=input("Enter name")
    print(student)    