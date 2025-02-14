#(print 1 to 10, its square roots in formatting.)
import math
for i in range(1,11):
    print('{0:5.2f} {1:7.4f}'.format(i,math.sqrt(i)))