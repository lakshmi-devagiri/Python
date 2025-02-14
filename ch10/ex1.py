#(Simple class with a function f())
#(self is the key word required for every function)
class MyClass:
    def f(self):
        return "hello from class"
x=MyClass()
y=x.f()
print(y)