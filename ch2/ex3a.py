# input food, drinks cost
# for food >= 2000, 20% for >= 1000 10% else 5%
# fror drinks >= 500 20%, for >= 200 10% else 5%
# find DISC, NET
food= float(input("enter the food price:"))
drinks= float(input("enter the drinks price:"))
if food>=2000 or drinks>=500:
    perc=20
elif food>=1000 or drinks>=200:
    perc=10
else:
    perc=5
disc=(perc/100)*food
disc1=(perc/100)*drinks
discount=disc+disc1
net=(food+drinks)-discount
print("food_discount:",disc)
print("drinks_discount1:",disc1)
print("total discount:",discount)
print("net:",net)

