a=int(input())
b=[int(s) for s in input().split()]
max=b[0]
for i in range(1,len(b)-1):
    if b[i]>max:
        max=b[i]

print(max)
    
