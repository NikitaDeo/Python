n=int(input("enter a num"))
def fibonacci_sequence(range_limit):
    sequence = []
    a, b = 0, 1
    while a <= range_limit:
        sequence.append(a)
        a, b = b, a + b
    return sequence
range_limit = int(input("Enter the range limit: "))
fib_sequence = fibonacci_sequence(range_limit)
print("Fibonacci sequence up to", range_limit, "is:", fib_sequence)