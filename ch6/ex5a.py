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
name=input("enter your name:")
n=len(name)
for i in range(0,n):
    print(name[0:i+1])