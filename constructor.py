class emp:
    def __init__(self,n,s) :
        self.name=n
        self.sal = s
    def putdata(self):
        print(self.name,self.sal)    
name=input("Enter name")
s=int(input("enter salary"))
e=emp(name,s)
e.putdata()        