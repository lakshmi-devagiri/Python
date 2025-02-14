# (Finding the average of an array)
a=[1,2,3,4,5,6]
sum=0
n=len(a)
for i in range(0,n):
    sum=sum+a[i]
av =sum/n
print("Average =",av)