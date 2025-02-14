'''
input your city:
Bangalore
o/p:
B
Ba
Ban
Bang
.
.
.
Bangalore
'''
name=input("Enter city Name:")
n=len(name)
for i in range(0,n):
    print(name[0:i+1])
    
