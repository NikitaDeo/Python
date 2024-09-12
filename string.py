def check_string_properties(s):
    print(any(char.isalnum() for char in s))

    print(any(char.isalpha() for char in s))

    print(any(char.isdigit() for char in s))

    print(any(char.islower() for char in s))

    print(any(char.isupper() for char in s))
s = input()
check_string_properties(s)