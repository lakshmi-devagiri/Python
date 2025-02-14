#(print multiplication table of a given number)
n=int(input("enter the multiplication number:"))
for i in range (1,11):
    print('%3d x %3d = %3d' % (n,i,i*n))
    