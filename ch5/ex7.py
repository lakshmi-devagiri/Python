#(Average example with n number of elements.)
def average(b):
    m=len(b)
    sum=0
    for x in b:
        sum=sum+x
    avg=sum/m
    return avg
n=int(input("enter the number of elemnts in an array "))
a=[]
for i in range(0,n):
    val=float(input("enter the element"))
    a.append(val)
c=average(a)
print("average",round(c,2) )