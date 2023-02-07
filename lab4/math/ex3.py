import math

print("Enter num of sides:")
num=int(input())
print("Enter len of sides:")
l=int(input())
area=(num*l*l)/(4*math.tan(math.pi/num))
print(area)