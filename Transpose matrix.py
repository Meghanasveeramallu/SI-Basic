a=[int(s) for s in input().split()]
b=[]
for i in range(a[0]):
    b.append([int(s) for s in input().split()])
c=[[0 for i in range(a[0])] for j in range(a[1])]
for i in range(a[1]):
    for j in range(a[0]):
        c[i][j]=b[j][i]
        print(b[j][i],end=" ")
    print()
