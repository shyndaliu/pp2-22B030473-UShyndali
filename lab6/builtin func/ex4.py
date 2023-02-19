import time
import math
print("enter n")
n=int(input())
print("enter ms")
tm=float(input())
time.sleep(tm/1000)
print("The answer is printed in {} ms, the answer is {}".format(tm,math.sqrt(n)))
