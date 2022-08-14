a=int(input())
b=[int(s) for s in input().split()]
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]==b[j]:
            print(b[i])
            break
