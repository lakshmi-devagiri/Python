# (Finding the maximum element of an array)
a = [10,50,45.32,89,67,11.11]
n=len(a)
mx=a[0]
for i in range(0,n):
    if a[i]>mx:
        mx=a[i]
print("maximum",mx)
