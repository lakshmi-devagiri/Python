#py (class called Circle with data as radius and function as area())
class Circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return 3.14*(self.r)**2
c=Circle(10.11)
a=c.area()
print("Radius =",c.r,"Area =",a)
c1=Circle(12.34)
a1=c1.area()
print("Radius =",c1.r,"Area =",a1)

