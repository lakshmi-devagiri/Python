#(tuples don’t allow their values to be changed.)
# (tuples are faster than lists.)
t = (12345, 54321, 'hello!') # paranthesis is used
print (t)
u = t, (1, 2, 3, 4, 5)
print (u)
#  wrong    t[0] = 88888 # Values inside a tuple cannot be changed. Hence tuple is faster than a list.
v = ([1, 2, 3], [3, 2, 1])
print (v)
print (v[0])
print("\n")
for x in v :
  for y in x :
    print (y, end=' ')
  print ("\n")