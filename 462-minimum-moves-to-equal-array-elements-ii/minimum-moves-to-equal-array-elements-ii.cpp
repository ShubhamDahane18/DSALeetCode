class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int moves = 0;
        int mid = n / 2;

        for(int i = 0; i < n; i++){
            moves += abs(nums[i] - nums[mid]);
        }
        
        return moves;
    }
};