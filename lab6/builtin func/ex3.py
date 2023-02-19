s=input()
s1=(''.join(reversed(s)))
if s==s1:
    print("Yep! Is a palindrome")
else:
    print("No")