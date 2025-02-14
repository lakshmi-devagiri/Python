#Python Program to Check if a Key Exists in a Dictionary or Not
d={'a':1,'b':2,'c':3,'d':4}
a=input("enter a Key:")
if a in d:
    print("key=",a,"value=",d[a])
else:
    print("key is not Present")