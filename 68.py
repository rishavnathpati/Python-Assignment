
class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def showarea(self):
        return self.length*self.breadth

    def showperimeter(self):
        return 2*(self.length+self.breadth)


l = int(input("Enter Length: "))
b = int(input("Enter breadth: "))
r = Rectangle(l, b)
print("Area: ", r.showarea())
print("Perimeter: ", r.showperimeter())
