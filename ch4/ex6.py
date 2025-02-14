# (lemda(n) = 1*2 + 2*3 + 3*4 +……. + n*(n+1)

def lemda(a):
    sum=0
    for i in range(0,a+1):
        sum=sum+i*(i+1)
    return sum

n=int(input("enter n value:"))  
c=lemda(n)
print("lemda =",c)