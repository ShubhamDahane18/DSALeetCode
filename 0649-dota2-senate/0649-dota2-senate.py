class Solution:

    def removeSenate(self, senate: list, ch: str, idx: int) -> bool:

        loopAround = False

        while True:
            if idx == 0:
                loopAround = True
            
            if senate[idx] == ch:
                senate.pop(idx)
                break
            idx = (idx + 1) % len(senate)
        
        return loopAround

    def predictPartyVictory(self, senate: str) -> str:
        
        senate = list(senate)
        R_count = senate.count('R')
        D_count = len(senate) - R_count

        idx = 0

        while R_count > 0 and D_count > 0:

            if senate[idx] == 'R':
                checkRemovalLeft = self.removeSenate(senate, 'D', (idx + 1) % len(senate))
                D_count -= 1

                if checkRemovalLeft:
                    idx -= 1
            
            else:
                checkRemovalLeft = self.removeSenate(senate, 'R', (idx + 1) % len(senate))
                R_count -= 1

                if checkRemovalLeft:
                    idx -= 1
            
            idx = (idx + 1) % len(senate)

        
        return "Dire" if R_count == 0 else "Radiant"