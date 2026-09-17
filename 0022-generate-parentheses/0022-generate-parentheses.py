class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        
        ans = []
        curr = []

        def solve(openL, closeL):

            if openL == closeL == n:
                ans.append("".join(curr))
                return
            
            if openL < n:
                curr.append("(")
                solve(openL + 1, closeL)
                curr.pop()
            
            if closeL < openL:
                curr.append(")")
                solve(openL, closeL + 1)
                curr.pop()
        
        solve(0, 0)
        return ans

        
