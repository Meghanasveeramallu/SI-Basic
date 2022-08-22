s=input()
n=''
for i in s:
    if i.islower():
        n+=i.upper()
    else:
        n+=i.lower()
print(n)
