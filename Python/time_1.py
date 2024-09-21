import time
current_time = time.time()
a=time.ctime(current_time)
print("current time is:=",a)
expiry=current_time+3600
print("expiry time ",time.ctime(expiry))
