class Solution:
    def partitionString(self, s: str) -> int:
        n = len(s)
        cnt = 0
        lastSeen = [-1] * 26

        subStrStart = 0

        for i in range(0, n):

            ch = s[i]

            if lastSeen[ord(ch) - ord('a')] >= subStrStart:

                cnt += 1
                subStrStart = i
            
            lastSeen[ord(ch) - ord('a')] = i
        
        return cnt + 1

            