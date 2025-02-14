# make a utility called sum
# to sum up the given arguments
# for example :     python sum.py 1.2 2 3.4
# o/p:              total = 6.6


import sys
print(sys.argv)
sum = 0
v = sys.argv
n = len(v)
for i in range(1,n):
    sum=sum+ float(v[i])
print("sum = " , sum)
