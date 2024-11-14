"""def count_digits(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count
number = int(input("Enter a number: "))
print("Number of digits:", count_digits(number))"""
n= int(input())
count=0
while n:
    count+=1
    n=n//10
print(count)