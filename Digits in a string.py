s=input()
x=0
n='0123456789'
for i in s:
    if i not in n:
        x=1
        break
        
if x==1:
    print("No")
else:
    print("Yes")
