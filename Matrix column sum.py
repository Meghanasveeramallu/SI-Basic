s=[int(s) for s in input().split()]
p=[]
for i in range(s[0]):
    l=[int(s) for s in input().split()]
    p.append(l)
su=0
for i in range(s[1]):
    for j in range(s[0]):
        su=su+p[j][i]
    print(su)
    su=0
    
