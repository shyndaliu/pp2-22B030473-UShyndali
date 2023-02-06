class Shape:
    def area(self):
        print()

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.len=a
        self.wid=b
    def area(self):
        print(self.len*self.wid)

figure=Rectangle(5, 6)
figure.area()