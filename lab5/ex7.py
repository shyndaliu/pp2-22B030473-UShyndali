import re
txt="some_variable_name"
ans=""
res=re.split(r"[_]",txt)
for i in res:
    ans+=i.capitalize()
print(ans)
