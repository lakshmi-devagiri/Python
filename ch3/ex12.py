# input a number n and print if it is prime or not

n=int(input("enter the n value"))

prime = True
for i in range(2, n):
    if(n%i==0):
      prime=False
      break

if(prime == True):
   print("PRIME")
else : 
   print("NOT PRIME")
        
