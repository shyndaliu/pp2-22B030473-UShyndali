import re
line="IWantSomeSpaces"
res=re.findall(r"[A-Z][a-z]*", line)
newlist=[]
for i in res:
    newlist.append(i.lower())
print('_'.join(newlist))
