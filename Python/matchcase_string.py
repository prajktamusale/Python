ch=str(input("1:Maharashtra\n 2:karnatak\n 3:kerala\n enter choice"))
match ch:
    case "Maharashtra":
        print("capital for maharashtra is Mumbai")
    case "karnatak":
        print("capital for karnataka is Banglore")
        
    case "kerala":
        print("capital for kerala is Tiruanantpuram")
        
    case '':
        print("Please enter the state name from the above list only ")     
        
