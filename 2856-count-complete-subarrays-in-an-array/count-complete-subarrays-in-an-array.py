class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        total = len(set(nums))
        mpp = {}
        l = 0
        r = 0
        n = len(nums)
        ans = 0

        while r < n:

            mpp[nums[r]] = mpp.get(nums[r], 0) + 1

            while len(mpp) == total:
                ans += n - r

                mpp[nums[l]] -= 1


                if mpp[nums[l]] == 0:
                    del mpp[nums[l]]
                
                l += 1
            
            r += 1
        
        return ans


