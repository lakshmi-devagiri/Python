f = open("C:\\MyPython\\ch8\\veg.txt","r") 
names=[]
prices=[]
while True:
    x=f.readline()
    if x=="":
        break
    x=x[:-1]
    names.append(x)
    y=f.readline()
    y=float(y)
    prices.append(y)
for i in range(0,len(names)):
    print(names[i],prices[i])
n=input("enter the no of Veg you want:")
kg=float(input("enter the no of kgs:"))
for i in range(0,len(names)):
    if n==names[i]:
        print(kg,"kg",n,"cost=",kg*prices[i])


