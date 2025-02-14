#complex class with init function
#(__init__ is a built in constructor)
class Complex:
    def __init__(self,real,imaginary):
        self.r=real
        self.i=imaginary
x=Complex(3.0,-0.3)
print("Real=",x.r,"Imaginary=",x.i)
        