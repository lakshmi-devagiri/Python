#(Raising user defined exception and handling it.)
try:
    hr = int(input("Enter hours:"))
    min = int(input("enter min:"))
    if min>=60:
        raise Exception("min are >= 60",str(min))
except Exception as e:
    print(e.args) # raised exception will also be caught here only.
else:
    print("TIME hr:{0} min:{1}".format(hr,min))
print("End of program")