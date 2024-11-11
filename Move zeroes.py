class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0  