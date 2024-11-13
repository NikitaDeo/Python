LI = [1, 2, 5, -33, 9, 5, 896, -55, 9, -5, 52, 633.5, 663056, 365, 61, 3, -4, 966, -5, 563, 5]
positive_numbers = [x for x in LI if x > 0]
negative_numbers = [x for x in LI if x < 0]
odd_numbers = [x for x in LI if isinstance(x, int) and x % 2 != 0]
even_numbers = [x for x in LI if isinstance(x, int) and x % 2 == 0]

sum_positive = sum(positive_numbers)
sum_negative = sum(negative_numbers)
sum_odd = sum(odd_numbers)
sum_even = sum(even_numbers)

print("Positive numbers:", positive_numbers)
print("Sum of positive numbers:", sum_positive)

print("Negative numbers:", negative_numbers)
print("Sum of negative numbers:", sum_negative)

print("Odd numbers:", odd_numbers)
print("Sum of odd numbers:", sum_odd)

print("Even numbers:", even_numbers)
print("Sum of even numbers:", sum_even)