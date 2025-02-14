#input a number and print if it is prime or not
def prime(a):
    flag=True
    for i in range(2,a+1):
        if a%i==0:
            flag=False
    if flag==True:
        print("Prime")
    else:
     print("Not Prime")    
n=int(input("enter n value:"))
c=prime(n)

