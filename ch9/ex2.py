#(exception handling for wrong input.)
try:
    x=int(input("enter x:"))
    print("You entered",x)
except ValueError:
    print("Wrong format entered")
print("end of the program")