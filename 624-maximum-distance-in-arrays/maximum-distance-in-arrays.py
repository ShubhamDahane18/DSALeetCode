class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        
        mn = arrays[0][0]
        mx = arrays[0][-1]
        ans = 0

        for i in range(1, len(arrays)):

            currMin = arrays[i][0]
            currMax = arrays[i][-1]

            ans = max(ans, abs(currMin - mx), abs(currMax - mn))

            mx = max(mx, currMax)
            mn = min(mn, currMin)
        
        return ans
        