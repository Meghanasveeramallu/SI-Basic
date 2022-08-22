s=input()
v='aAeEiIoOuU'
v_c=0
c_c=0
for i in s:
    if i in v:
        v_c+=1
    else:
        c_c+=1
if c_c==0:
    print("Yes")
else:
    print("No")
