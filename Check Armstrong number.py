n=int(input())
m=n
sum=0
while(n>0):
    rem=n%10
    sum=sum + (rem*rem*rem)
    n=n//10
if (sum==m):
    print("Yes")
else:
    print("No")
