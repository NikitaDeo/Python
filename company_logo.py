from collections import Counter

def top_three_characters(s):
    char_count = Counter(s)
    sorted_characters = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    for char, count in sorted_characters[:3]:
        print(char, count)
if __name__ == "__main__":
    s = input().strip()
    top_three_characters(s)