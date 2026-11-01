class Solution {
public:
    int minMoves(vector<int>& nums) {
        int n = nums.size();
        int ops = 0;
        // int minEle = **min_element(nums.begin(), nums.end());
        int minEle = nums[0];
        for(int num: nums){
            if(num < minEle){
                minEle = num;
            }
        }
        for(int i = 0; i < n; i++){
            ops += (nums[i] - minEle);
        }

        return ops;
    }
};