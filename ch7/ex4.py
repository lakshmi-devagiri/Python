#(printing 1 to 10, squares and cubes with another style of formatting)
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
    print('{0:3d} {1:4d}{2:5d}'.format(i,i*i,i*i*i))