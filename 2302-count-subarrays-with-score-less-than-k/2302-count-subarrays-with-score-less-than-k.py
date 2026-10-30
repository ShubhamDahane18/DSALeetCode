class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        s = 0
        score = 0 
        ans = 0

        while r < n:
            s += nums[r]
            score = s * (r - l + 1)

            while score >= k:
                s -= nums[l]
                l += 1
                score = s * (r - l + 1)
            ans += (r - l + 1)
            r += 1
        
        return ans