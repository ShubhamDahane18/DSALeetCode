class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        rounds = 0

        mpp = {}

        for task in tasks:
            mpp[task] = mpp.get(task, 0) + 1
        

        for task, count in mpp.items():

            if count == 1:
                return -1
            
            if count % 3 == 0:
                rounds += count // 3
            
            else:
                rounds += (count // 3) + 1
        

        return rounds