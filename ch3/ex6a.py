# sigma = 1+2+3+.......+n
# n is the input.
# output sigma
n=int(input("enter the n value:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum :",sum)
