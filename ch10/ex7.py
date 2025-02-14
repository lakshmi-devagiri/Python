#(Sphere is the class with radius as data and 
# volume(), area() are functions.
class Sphere:
    def __init__(self,radius):
        self.r=radius
    def volume(self):
        return (4/3)*3.14*(self.r)**3
    def area(self):
        return 4*3.14*(self.r)**2
s=Sphere(10)
v=s.volume()
a=s.area()
print("Radius=",s.r,"Volume=",v,"Area=",a)
       