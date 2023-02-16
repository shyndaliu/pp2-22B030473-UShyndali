import re
line="IWantSomeSpaces"
res=re.findall(r"[A-Z][a-z]*", line)
print(' '.join(res))