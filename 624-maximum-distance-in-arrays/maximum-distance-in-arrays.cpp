class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        // int MIN = arrays[0][0];
        int MIN = arrays[0].front();
        
        int MAX = arrays[0].back();
        // int MIN = arrays[0][arrays[0].size() - 1];
        int res = 0;

        for(int i = 1; i < arrays.size(); i++){
            int currMin = arrays[i][0];
            int currMax = arrays[i].back();

            res = max({res, abs(currMax - MIN), abs(currMin - MAX)});
            MAX = max(currMax, MAX);
            MIN = min(currMin, MIN);
        }

        return res;

    }
};