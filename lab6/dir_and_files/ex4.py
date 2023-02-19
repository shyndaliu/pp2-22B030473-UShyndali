f=open(r"U:\всё\учеба\2022-2023\pp2\pp2-22B030473-UShyndali\lab6\dir_and_files\sometext.txt")
cnt=0
for lines in f:
    cnt+=1
print("files has {} lines".format(cnt))