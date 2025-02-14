# Python Program to Add a Key-Value Pair to the Dictionary
d ={'a':1,'b':2,'c':3,'d':4}
k = input("enter a key:") #key has to be string. it cannot be a number
v = int(input("enter the key value:"))
d[k] = v
print(d)