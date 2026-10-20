class Solution {
public:

    bool removeSenator(string &senate, char ch, int idx){
        bool loopAround = false;

        while(true){
            if(idx == 0){
                loopAround = true;
            }

            if(senate[idx] == ch){
                senate.erase(senate.begin() + idx);
                break;
            }

            idx = (idx + 1) % senate.size();
            
        }

        return loopAround;
    }

    string predictPartyVictory(string senate) {
        int Rcount = count(senate.begin(), senate.end(), 'R');
        int Dcount = senate.length() - Rcount;

        int idx = 0;

        while(Rcount > 0 && Dcount > 0){
            
            if(senate[idx] == 'R'){
                bool checkRemovalLeft =  removeSenator(senate, 'D', (idx + 1) % senate.size());
                Dcount--;

                if(checkRemovalLeft){
                    idx--;
                }
            }
            else{
                bool checkRemovalLeft = removeSenator(senate, 'R', (idx + 1) % senate.size());
                Rcount--;

                if(checkRemovalLeft){
                    idx--;
                }
            }

            idx = (idx + 1) % senate.size();
        }

        return Rcount == 0 ? "Dire" : "Radiant";
    }
};