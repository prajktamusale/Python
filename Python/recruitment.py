Gender = 'F'
Gender = 'M'

if(Gender == 'M'):
    
    a =int(input("Enter your Age"))
    h =int(input("Enter your height"))
    if((a>=25 and a<=30) and h>=160):
        print("You are qualified for this position")
else:
    print("you are not qualified for this posotion")
    
if(Gender == 'F'):
    
    a =int(input("Enter your Age"))
    h =int(input("Enter your height"))
    if((a>=20 and a<=25) and h>=155):
        print("You are qualified for this position")
else:
    print("you are not qualified for this posotion")
        