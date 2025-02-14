'''hotel bill example
i/p bill, perc
o/p discount, net
'''
bill= float(input("enter the bill amount"))
perc = float(input("enter the Percentage"))
discount = bill*perc/100
net= bill- discount
print("discount=",discount)
print("net=", net)
