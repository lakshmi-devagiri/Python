 #(Input a 3 digit number and find the sum of all the digits)
a=int(input("enter a three digit number")) # ex: 234
d1=a%10
d2=(a%100)//10
d3=a//100
s= d1+ d2 + d3
print("sum =",s)
