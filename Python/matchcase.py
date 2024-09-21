ch=int(input("1:addition\n 2:Subtraction\n 3:division\n enter choice"))
a=int(input("enter number1"))
b=int(input("enter number2"))
match ch:
    case 1:
        c=a+b
        print("result is ",c)
    case 2:
        c=a-b
        print("result is",c)
    case 3:
        c=a/b
        print("result is ",c)
    case '':
        print("Invalid input")     
        
               