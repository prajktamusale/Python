class student:
    def get(self):
        self.roll=input("Enter roll number")
        self.marks=int(input("enter marks"))
    def put(self):
        print("roll",self.roll,self.marks)
class result(student):
    def display_result(self):
        if self.marks>35:
            print("student is pass")
        else:
            print("student is fail")
            
class grade(result):
    pass
class sports(result,student):
    pass
s1=result()

s1.get()
s1.put()
s1.display_result()

            