#(catching division by zero error.)
try:
    x = int(input("Enter a number:"))
    y = int(input("Enter another number:"))
    z = x/y
    print("quotient = ",z)
except ZeroDivisionError:
    print("denominator is zero")
print("End of program")