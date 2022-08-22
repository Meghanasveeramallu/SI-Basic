def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

n,k=map(int,input().split())
a=[int(s) for s in input().split()]
if (binarySearch(a, 0, len(a)-1, k)!=-1):
    print("true")
else:
    print("false")
