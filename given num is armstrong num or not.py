n=int(input())
a=n
m=str(n)
digit=len(m)
sum=0
while n:
    d=n%10
    cube=d**digit
    sum+=cube
    n=n//10
if a==sum:
    print("Armstrong")
else:
    print("Not Armstrong")