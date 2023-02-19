import os
p=os.listdir(r"U:\всё\учеба\2022-2023\pp2")
for i in p:
    if os.path.isdir(i):
        print(i)
for i in p:
    if os.path.isdir(i) or os.path.isfile(i):
        print(i)
for i in p:
    if os.path.isfile(i):
        print(i)