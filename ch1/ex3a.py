'''hotel bill example
i/p bill, perc
o/p discount, net
'''
bill = float(input("Enter the bill amount"))
perc = float(input("Enter the percentage"))
discount = bill*perc/100
net = bill-discount
print("Discount",discount)
print("Net",net)