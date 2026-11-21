class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        temp = []

        for i in range(n):

            temp.append((abs(arr[i] - x), arr[i]))
        
        temp.sort()
        ans = []

        for i in range(k):
            ans.append(temp[i][1])
        
        ans.sort()

        return ans
