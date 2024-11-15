n = int(input("Enter the number:"))
def count_digits(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count
number = 123456
print("Number of digits:", count_digits(number))
