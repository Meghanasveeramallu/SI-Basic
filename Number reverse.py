N=int(input())
neg=0
rev=0
if N<0:
    neg=1
    N=N*(-1)
while N>0:    
    rev=rev*10+N%10
    N=N//10
if neg==0:
    print(rev)
else:
    print((-1)*rev)
