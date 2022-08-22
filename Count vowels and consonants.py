s=input()
v='aAeEiIoOuU'
v_c=0
c_c=0
for i in range(len(s)):
    if s[i] in v:
        v_c+=1
    else:
        c_c+=1
print(v_c,c_c)
