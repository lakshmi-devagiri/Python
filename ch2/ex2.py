#Input hotel bill, give 10% for Rs 100 or more other wise give 5% discount. 
# Calculate the discount amount and net bill
bill = float(input("enter the bill"))
if(bill>=100):
    perc=10
else:
    perc=5

discount = bill*perc/100 
net = bill-discount
print("discount =",discount)
print("net =",net)
