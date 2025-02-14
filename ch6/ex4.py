'''
(print as specified)
 rao
 r 
 a 
 o 
 oar 
'''
name=input("enter your Name:")
print(name)
n=len(name)
for i in range(0,n):
    print(name[i])
for i in range(n-1,-1,-1):
    print(name[i], end="")
