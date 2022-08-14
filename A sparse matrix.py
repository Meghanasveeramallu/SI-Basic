a=[int(s) for s in input().split()]
b=[]
for i in range(a[0]):
    b.append([int(s) for s in input().split()])
count=0
for i in range(a[0]):
    for j in range(a[1]):
        if (b[i][j]==0):
            count+=1
if count>int(a[0]*a[1]/2):
    print("Yes")
else:
    print("No")
