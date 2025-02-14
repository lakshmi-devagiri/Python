#print 1 to 10 , squares and cubes as specified below.
'''
 1   1    1
 2   4    8
 3   9   27
.
.
.
10 100 1000
'''
for i in range(1,11):
    print(repr(i).rjust(3),repr(i*i).rjust(3),repr(i*i*i).rjust(5))