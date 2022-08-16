n=int(input())
c=0
m=n
suma=0
while(n>0):
    n=n//10
    c+=1
n=m
while(n>0):
    rem=n%10
    suma=suma+pow(rem,c)
    n=n//10
    #print(n,suma)
    
if (suma==m):
    print("Yes")
else:
    print("No")
