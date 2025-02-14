#(Input a 3 digit number and find the sum of all the digits)
a = int(input("Enter a 4 digit number"))
d1=a%10
print("d1",d1)
d2=a%100//10
print("d2",d2)
d3=a%1000//100
print("d3",d3)
d4=a//1000
print("d4",d4)
y = d1+d2+d3+d4
print("y",y)

