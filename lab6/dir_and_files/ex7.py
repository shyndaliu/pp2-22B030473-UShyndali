f1=open("icopiedfromhere.txt", "r")
f2=open("tohere.txt", "w")
for line in f1:
    f2.write(line)