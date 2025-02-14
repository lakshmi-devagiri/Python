#(Finding the maximum of an array using a function.)
arr = [10,50,45.32,89,67,11.11]
def maximum(b):
    n=len(b)
    mx=b[0]
    for i in range(0,n):
        if b[i]>mx:
           mx=b[i]
    return mx
max=maximum(arr)
print("Maximum",max)
