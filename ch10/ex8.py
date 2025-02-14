# Rectangle example
class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        return (self.l)*(self.b)
r=Rectangle(12,10)
a=r.area()
print("Length =",r.l,'Breadth=',r.b,"Area=",a)