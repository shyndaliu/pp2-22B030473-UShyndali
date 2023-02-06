class C1:
    def __init__(self):
        self.str=""
    def getstr(self):
        self.str=input()
    def printstr(self):
        print(self.str.upper())

x=C1()
x.getstr()
x.printstr()