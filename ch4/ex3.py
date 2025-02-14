# (function to find the maximum of 2 numbers.)
def maximum(x,y):
    if x>y:
        return x
    else:
        return y 
    
a=float(input("enter a:"))
b=float(input("enter b:"))
c=maximum(a,b)
print("Max =",c)