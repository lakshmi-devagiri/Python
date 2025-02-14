#(printing in floating point formats)
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
    print('{0:5.2f} {1:6.2f} {2:7.2f}'.format(i,i**2,i**3))