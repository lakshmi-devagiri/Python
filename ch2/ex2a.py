#Input hotel bill, give 10% for Rs 100 or more other wise give 5% discount. 
# Calculate the discount amount and net bill
bill = int(input("enter the hotel bill"))

if bill>=100:
    perc=10
else:
    perc=5
discount =(perc/100)*bill
net=bill-discount
print("discount",discount)
print("net",net)