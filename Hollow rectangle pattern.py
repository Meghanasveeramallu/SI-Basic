a=[int(s) for s in input().split()]
w=a[0]
l=a[1]
for i in range(l):
    if i==0 or i==(l-1):
        print(w*"*",end='')
    else:
        for j in range(0,w):
            if j==0 or j==w-1:
                print("*",end='')
            else:
                print(" ",end='')
    print()
