class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        start = 0

        for i in range(n):

            if nums[i] != 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1 