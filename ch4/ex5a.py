# (sigma(n) = 1 + 2 + 3 + …… + n)
def sigma(a):
    sum=0
    for i in range(0,a+1):
        sum=sum+i
    return sum
n=int(input("enter n value:"))
c=sigma(n)
print("sum:",c)