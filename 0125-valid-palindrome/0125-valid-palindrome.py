class Solution:

    def isAlpha(s, i):
        # a-z, 0-9
        x = ord(s[i])
        if 97<=x<=122 or 48<=x<=57:
            return True
        else:
            return False    

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        i = 0
        j = n - 1

        while i < j:

            if not s[i].isalnum():
                i += 1
                continue
            
            if not s[j].isalnum():
                j -= 1
                continue

            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True
    



        