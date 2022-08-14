a=[int(s) for s in input().split()]
c=[0 for i in range(a[0])]
d=[0 for i in range(a[0])]
for i in range(a[0]):
    c[i]=[int(s) for s in input().split()]
for i in range(a[0]):
    d[i]=[int(s) for s in input().split()]

r=[[0 for i in range(a[1])] for j in range(a[0])]
for i in range(a[0]):
    for j in range(a[1]):
        r[i][j]=c[i][j]+d[i][j]
        print(r[i][j],end=" ")
    print()
