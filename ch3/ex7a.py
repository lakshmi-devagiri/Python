# theta = 1/1 + 1/2 + 1/3 + ...... + 1/n
# n is the input.
# output theta
n = int(input("enter the n value"))
theta=0
for i in range(1,n+1):
    theta=theta+1/i
print("theta:",theta)
