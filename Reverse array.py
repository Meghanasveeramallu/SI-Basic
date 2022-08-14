a=int(input())
b=[int(s) for s in input().split()]
for i in range(len(b)-1,-1,-1):
    print(b[i],end=" ")
