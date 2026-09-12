class Solution {
public:
    int partitionString(string s) {
        int n = s.size();
        int cnt = 0;
        vector<int> lastSeen(26, -1);
        int substrstart = 0;

        for(int i = 0; i < n; i++){
            char ch = s[i];

            if(lastSeen[ch - 'a'] >= substrstart){
                cnt++;
                substrstart = i;
            }
            lastSeen[ch - 'a'] = i;
        }

        return cnt + 1;
    }
};