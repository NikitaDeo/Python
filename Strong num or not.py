n=int(input())
m=n
fact=1
sum=0
while n:
    d=n%10
    for i in range(1,d+1,1):
        fact=fact*i
    sum+=fact
    fact=1
    n=n//10
if sum==m:
    print("strong")
else:
    print("not strong")