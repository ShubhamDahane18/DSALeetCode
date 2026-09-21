class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        n = len(nums)
        ans = nums[0]
        currSum = 0

        for i in nums:
            currSum += i

            if currSum > ans:
                ans = currSum
            
            if currSum < 0:
                currSum = 0
        
        return ans
        