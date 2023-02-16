import re
with open("row.txt") as myfile:
    for line in myfile:
        res=re.sub(r"[, .]", ":", line)
        print(res)