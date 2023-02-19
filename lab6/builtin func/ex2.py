s="ThisIsMyString"
cnt1=0
cnt2=0
for i in s:
    if(i.isupper()):
        cnt1+=1
    elif(i.islower()):
        cnt2+=1
print("Uppercase:", cnt1)
print("Lowercase:", cnt2)