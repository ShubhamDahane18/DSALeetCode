class Solution {
public:
    int minMoves(vector<int>& nums) {
        int n = nums.size();
        // int s = accumulate(nums.begin(), nums.end(), 0);
        // int minEle = *min_element(nums.begin(), nums.end());
        int s = 0;
        // int minEle = INT_MAX;
        int minEle = nums[0];
        for(int num: nums){
            s += num;
            minEle = min(num, minEle);
        }

        return s - n * minEle;
    }
};