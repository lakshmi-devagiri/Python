#(print 1 to 10, its square roots in formatting.)
import math
for i in range(1,11):
    print('%5.2f %7.4f' %(i,math.sqrt(i)))