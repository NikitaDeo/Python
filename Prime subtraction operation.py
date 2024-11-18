from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return [x for x in range(2, n + 1) if is_prime[x]]
        
        primes = sieve(1000)  
        prev = 0 
        for num in nums:
            for p in reversed(primes):
                if num - p > prev:
                    num -= p
                    break
            if num <= prev:
                return False
            prev = num 
        
        return True  