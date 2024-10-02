from collections import defaultdict

def wonderfulSubstrings(word):
    # Dictionary to store counts of each bitmask
    freq = defaultdict(int)
    freq[0] = 1  # Initialize with empty bitmask (all even)

    current_mask = 0
    wonderful_count = 0

    for char in word:
        # Toggle the bit for the current character
        current_mask ^= 1 << (ord(char) - ord('a'))

        # Check if current mask is already wonderful (i.e., freq[current_mask] exists)
        wonderful_count += freq[current_mask]

        # Check if flipping exactly one bit can make it wonderful
        for i in range(10):  # There are 10 characters from 'a' to 'j'
            wonderful_count += freq[current_mask ^ (1 << i)]

        # Update the frequency of the current bitmask
        freq[current_mask] += 1

    return wonderful_count

# Test cases

# Case 1: word = "aba"
word1 = "aba"
print(f"Case 1: Wonderful substrings = {wonderfulSubstrings(word1)}")  # Expected output: 4

# Case 2: word = "aabb"
word2 = "aabb"
print(f"Case 2: Wonderful substrings = {wonderfulSubstrings(word2)}")  # Expected output: 9

# Case 3: word = "he"
word3 = "he"
print(f"Case 3: Wonderful substrings = {wonderfulSubstrings(word3)}")  # Expected output: 2
