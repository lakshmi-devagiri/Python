# Python Program to Find the Sum of All the Items in a Dictionary
d ={'a':1,'b':2,'c':3,'d':4}
s = 0
for x in d.keys():
    s = s + d[x]
print("sum of values:",s)
print("sum of values:",sum(d.values()))