class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken_set = set(brokenLetters)
        count = 0

        for word in text.split():
            if not any(char in broken_set for char in word):
                count += 1

        return count
