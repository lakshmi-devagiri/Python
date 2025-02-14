#(multiplication table with formatting)
n=int(input("enter a number:"))
for i in range(1,11):
    print(repr(n).rjust(3),"x",repr(i).rjust(3),"=",repr(n*i).rjust(3))