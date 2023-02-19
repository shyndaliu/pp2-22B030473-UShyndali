import os
p=os.listdir(r"U:\всё\учеба\2022-2023\pp2\pp2-22B030473-UShyndali")

print('Exists:', os.access(__file__, os.F_OK))
print('Readable:', os.access(__file__, os.R_OK))
print('Writable:', os.access(__file__, os.W_OK))
print('Executable:', os.access(__file__, os.X_OK))