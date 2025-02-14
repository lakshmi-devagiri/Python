#(Same as above example, using 
#(set example. Sets don’t have duplicate values.)
a = ['tomato', 'orange', 'apple']
b = set(a)
print (b)
c = 'orange' in b
print ("orange is there = ", c)
x = set(['coconut', 'orange'])
print ("b = " , b)
print ("x = " , x)
print ("b - x = ",end= ' ')
print (b - x)
print ("b | x = ",end=' ')
print (b | x)
print ("b & x = ",end=' ')
print (b & x)