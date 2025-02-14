#Python Program to Find Second Largest Number in a List
def maximum(b):
    m=len(b)
    mx=b[0]
    for x in b:
        if x>mx:
            mx=x
    return mx

n=int(input("enter the number of elemnts in an array "))
a=[]
for i in range(0,n):
    val=float(input("enter the element"))
    a.append(val)
c=maximum(a)
a.remove(c)
second_Max=maximum(a)
print("Maximum =",round(c,2) )
print("Second-Maximum =",round(second_Max,2) )
