n=int(input())
for i in range(n):
    if i==0:
        print(n*"* ",end='')
    else:
        for j in range(n):
            if j==0 or j==n-i-1:
                print("* ",end='')
            else:
                print("  ",end='' )
    print()
