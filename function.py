def is_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
def main():
    year = int(input("Enter a year: "))
    print("True" if is_leap(year) else "False")
if __name__ == "__main__":
    main()
