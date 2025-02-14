
#(abs(n) function always returns a positive value.)
def absolute(a):
    if a<0:
        a=-a
    return a
n=float(input("enter n value:"))  
c=absolute(n)
print("absolute =",c)