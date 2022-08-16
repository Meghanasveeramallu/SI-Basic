import math
n=int(input())
flag=0
if n>1:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            print("No")
            flag=1
            break
    if flag==0:
        print("Yes")
elif n==1:
    print("No")
    
