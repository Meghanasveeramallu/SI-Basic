def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
 
n,k=map(int,input().split())
a=[int(s) for s in input().split()]
print(search(a, n, k))
