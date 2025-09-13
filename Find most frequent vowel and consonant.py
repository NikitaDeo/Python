class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        vowels = set('aeiou')
        vowel_freq = {}
        consonant_freq = {}

        for char in s:
            if char in vowels:
                vowel_freq[char] = vowel_freq.get(char, 0) + 1
            else:
                consonant_freq[char] = consonant_freq.get(char, 0) + 1

        max_vowel = max(vowel_freq.values()) if vowel_freq else 0
        max_consonant = max(consonant_freq.values()) if consonant_freq else 0

        return max_vowel + max_consonant
