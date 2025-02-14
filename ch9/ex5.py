#(exception with else block.)
try:
    x = int(input("enter a number:"))
    y = int(input("enter another number:"))
    z = x/y
except Exception as e:
    print(e.args)
else:
    print("quotient = ",z)
print("End of program")