#((multiple exception handling, also catching general Exception.)
try:
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    z = x/y
    print("quotient = ",z)
except ZeroDivisionError:
    print("denominator is zero")
except Exception as e:
    print(e.args)
print("End of program")