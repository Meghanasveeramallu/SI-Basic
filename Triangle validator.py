a=[int(s) for s in input().split()]
if ((a[0]+a[1]>a[2]) and (a[2]+a[1]>a[0]) and (a[0]+a[2]>a[1])):
    print("Yes")
else:
    print("No")
