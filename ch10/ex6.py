#(class called Cone with data as radius and height,
#  and volume() is the function.)
class Cone:
    def __init__(self,radius,height):
        self.r=radius
        self.h=height
    def volume(self):
        return (1/3)*3.14*self.r *self.r*self.h
c=Cone(10,5)
v=c.volume()
print("Radius=",c.r," Height=",c.h,"Volume=",v)

        