#Solving a quadratic equation: ax^2 + bx + c = 0)
#a, b, c are inputs)   
#(Roots of the equation are x1, x2 are outputs.
#This solution takes care of imaginary roots also)
# Quadratic Equation 
# ax^2 + bx + c = 0 
# x1 = (-b + sqrt(b^2 - 4ac))/(2a) 
# x2 = (-b - sqrt(b^2 - 4ac))/(2a)
# x1 and x2 are the roots of given equation
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b*b - 4*a*c
if d >= 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print("The roots are ", x1, " & ", x2)
else: 
    print("real = ",-b/(2*a),"imag = +",math.sqrt(-d)/(2*a),"i")
    print("real = ",-b/(2*a),"imag = -",math.sqrt(-d)/(2*a),"i")