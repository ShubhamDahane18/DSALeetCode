class Solution {
public:
    int n;

    void removeSenator(string &senate, vector<bool> &removed, char ch, int idx){

        while(true){

            if(senate[idx] == ch && removed[idx] == false){
                removed[idx] = true;
                break;
            }

            idx = (idx + 1) % senate.size();
            
        }

    }

    string predictPartyVictory(string senate) {
        int n = senate.size();

        int Rcount = count(senate.begin(), senate.end(), 'R');
        int Dcount = senate.length() - Rcount;

        vector<bool> removed(n, false);

        int idx = 0;

        while(Rcount > 0 && Dcount > 0){

            if(removed[idx] == false){

                if(senate[idx] == 'R'){
                    removeSenator(senate, removed, 'D', (idx + 1) % senate.size());
                    Dcount--;
                   
                }
                else{
                    removeSenator(senate, removed, 'R', (idx + 1) % senate.size());
                    Rcount--;

                }
            }
            
            idx = (idx + 1) % senate.size();
        }

        return Rcount == 0 ? "Dire" : "Radiant";
    }
};