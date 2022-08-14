a=int(input())
b=[int(s) for s in input().split()]
s=0
for i in range(len(b)):
    if b[i]%2==1:
        s=s+b[i]
print(s)
