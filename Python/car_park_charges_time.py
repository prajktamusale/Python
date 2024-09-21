import time
a=eval(input("Enter hours"))
if(a<=2):
    current_time = time.time()
    a=time.ctime(current_time)
    print("current time is:=",a)
    expiry=current_time+3600
    print("expiry time ",time.ctime(expiry))
    print("Charges for 2 hours is $3.50")
if(a>2 and a<4):
    current_time = time.time()
    a=time.ctime(current_time)
    print("current time is:=",a)
    expiry=current_time+3600
    print("expiry time ",time.ctime(expiry))
    print("Charges for 4 hours is $5.0")
    