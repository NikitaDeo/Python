def minSubarray(nums, p):
    total_sum = sum(nums)
    remainder = total_sum % p

    if remainder == 0:
        return 0 

    prefix_sum_mod = {0: -1} 
    current_sum = 0
    min_length = len(nums)

    for i, num in enumerate(nums):
        current_sum += num
        current_mod = current_sum % p
        target_mod = (current_mod - remainder) % p

        if target_mod in prefix_sum_mod:
            min_length = min(min_length, i - prefix_sum_mod[target_mod])

        prefix_sum_mod[current_mod] = i

    return min_length if min_length < len(nums) else -1
