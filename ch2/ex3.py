# input food, drinks cost
# for food >= 2000, 20% for >= 1000 10% else 5%
# fror drinks >= 500 20%, for >= 200 10% else 5%
# find DISC, NET

food = float(input("enter the Food cost"))
drinks = float(input("enter the drinks cost"))
if(food >= 2000):
    perc = 20
elif(food >= 1000):
    perc=10
else:
    perc=5
if(drinks >= 500):
    perc1=20
elif(drinks >=200):
    perc1=10
else:
    perc1=5
disc = food*perc/100
disc1= drinks*perc1/100
discount= disc+disc1
net = food+drinks-discount
print("discount",discount)
print("net",net)






