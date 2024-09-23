#The called function is passed as an argument to the caller function.
def called(n):
    return n[0]*n[1]

def caller(func, n):
    return func(n)

num = (8,5)
ans = caller(called, num)
print("Multiplication = ", ans)