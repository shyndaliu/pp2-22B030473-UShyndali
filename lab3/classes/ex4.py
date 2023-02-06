class Point:
    def __init__(self, a, b):
        self.x=a
        self.y=b
    def show(self):
        print(self.x, self.y)
    def move(self, newx, newy):
        self.x=newx
        self.y=newy
    def dist(self, secondx, secondy):
        print(pow((self.x-secondx)**2+(self.y-secondy)**2,0.5))

coordinate=Point(0,0)
coordinate.show()
coordinate.move(5,7)
coordinate.show()
coordinate.dist(5,9)

"""a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points"""