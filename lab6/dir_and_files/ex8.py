import os
p=(r"U:\всё\учеба\2022-2023\pp2\pp2-22B030473-UShyndali\lab6\dir_and_files\thisfieiswillbedeleted.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")