class Solution:
    def lexicalOrder(self, n):
        result = []
        num = 1
        for _ in range(n):
            result.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        return result
solution = Solution()
n1 = 13
print("Case 1: {}".format(solution.lexicalOrder(n1)))
n2 = 2
print("Case 2: {}".format(solution.lexicalOrder(n2)))