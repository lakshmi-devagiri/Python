#Finding the average of an array using a function.
a = [13,17,18.93,55.55,23]

def average(b):
    n=len(b)
    sum=0
    for i in range(0,n):
        sum=sum+b[i]
    av=sum/n
    return av
avg=average(a)
print("Average =",avg)
        