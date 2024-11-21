"""def is_magic_number(num):
    def sum_of_digits(n):
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total
    while num >= 10:
        num = sum_of_digits(num)
    return num == 1
number = 55
if is_magic_number(number):
    print(f"{number} is a MAGIC number.")
else:
    print(f"{number} is NOT a MAGIC number.")"""

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