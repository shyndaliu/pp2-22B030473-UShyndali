class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, a):
        super().__init__()
        self.len=a
    def area(self):
        print(self.len*self.len)

figure=Square(5)
figure.area()