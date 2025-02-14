#(Raising user defined exception and handling it.)
try:
    feet = int(input("Enter feet:"))
    inches = float(input("enter inches:"))
    if inches>=12.0:
        raise Exception("inches are >= 12",str(inches))
except Exception as e:
    print(e.args) # raised exception will also be caught here only.
else:
    print("Height Feet:{0} Inches:{1}".format(feet,inches))
print("End of program")