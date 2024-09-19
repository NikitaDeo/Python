def print_rangoli(size):
    alphabet = [chr(97 + i) for i in range(size)]
    lines = []
    for i in range(size):
        row_letters = alphabet[size-1:i:-1] + alphabet[i:size]
        row = '-'.join(row_letters).center(4*size - 3, '-')
        lines.append(row)
    print('\n'.join(lines + lines[-2::-1]))
if __name__ == "__main__":
    size = int(input().strip())
    print_rangoli(size)
