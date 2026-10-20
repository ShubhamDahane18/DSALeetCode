class Solution:

    def removeSenate(self, senate: list, removed: list, ch: str, idx: int) -> bool:

        while True:   
            
            if senate[idx] == ch and removed[idx] == False:
                removed[idx] = True
                break
            idx = (idx + 1) % len(senate)
        

    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        senate = list(senate)
        R_count = senate.count('R')
        D_count = len(senate) - R_count

        removed = [False] * n

        idx = 0

        while R_count > 0 and D_count > 0:

            if removed[idx] == False:

                if senate[idx] == 'R':
                    self.removeSenate(senate, removed, 'D', (idx + 1) % len(senate))
                    D_count -= 1
                
                else:
                    self.removeSenate(senate, removed, 'R', (idx + 1) % len(senate))
                    R_count -= 1
                
            idx = (idx + 1) % len(senate)

        
        return "Dire" if R_count == 0 else "Radiant"