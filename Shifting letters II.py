class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shift_array = [0] * (n + 1)
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            shift_array[start] += shift_value
            shift_array[end + 1] -= shift_value
        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]
        result = []
        for i in range(n):
            net_shift = shift_array[i] % 26 
            new_char = chr((ord(s[i]) - ord('a') + net_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)
solution = Solution()
s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
print(solution.shiftingLetters(s, shifts)) 
s = "dztz"
shifts = [[0, 0, 0], [1, 1, 1]]
print(solution.shiftingLetters(s, shifts)) 
