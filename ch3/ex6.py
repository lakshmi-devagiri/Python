# sigma = 1+2+3+.......+n
# n is the input.
# output sigma
n=int(input("enter the n value:"))
sigma= 0
for i in range(0,n+1):
    sigma=sigma+i
print("sigma=",sigma)
  