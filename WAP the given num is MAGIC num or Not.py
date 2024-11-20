n=int(input("Enter the number"))
while n>9:
        sum=0
        temp=n
        while n:
            d=n%10
            sum+=d
            n=n//10
        n=sum
if n==1:
        print("MAGIC")
else:
        print("NOT MAGIC")
