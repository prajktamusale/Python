class A:
    def get(self):
        self.a=int(input("enter number"))
        print("a ",self.a)
        
class B:
    def get_b(self):
        self.b=int(input("enter b"))
        print(" b",self.b)
        a1=A()
        a1.get() 
    def put(self):
        print("***")
                   
b1=B()
b1.get_b()                   