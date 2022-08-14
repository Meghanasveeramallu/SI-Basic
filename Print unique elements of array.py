a=int(input())
b=[int(s) for s in input().split()]
freq = {}
for item in b:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

for i in freq:
    if freq[i]==1:
        print(i,end=" ")
