#(print the name in reverse way)
name=input("enter your name:")
n=len(name)
for i in range(n-1,-1,-1):
    print(name[i],end="")
