f = open("C:\\MyPython\\ch8\\veg.txt","r") 
#create the file veg.txt in visual studio
names=[]
costs = []
while True:
    x = f.readline()
    if x == "": break
    x =x[:-1] 
    #if x is not null, remove the last character and append x.
    names.append(x)
    y = f.readline()
    y = float(y)
    costs.append(y)
for i in range(0,len(names)):
    print(names[i],costs[i])