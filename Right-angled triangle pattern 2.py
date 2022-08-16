n=int(input())
for i in range(n):
    diff=n-1
    val=i+1
    for j in range(i+1):
        print(val,end=' ')
        val+=diff
        diff-=1
    print()
