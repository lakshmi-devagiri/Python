# Python Program to Remove Odd Indexed Characters in a string
s=input("enter a sentence:")
s1=""
n=len(s)
for i in range(0,n,2):
   s1=s1+s[i]
print(s1)


