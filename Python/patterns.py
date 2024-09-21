#for i in range(1,5):
  #  for j  in range (1,i+1):
#        print(j,end=" ")
 #   print()  
n=1 
for i in range(1,5):
        for j  in range (n+i-1,n-1, -1):
            print(j,end=" ")
            
        print()  
        n+=i