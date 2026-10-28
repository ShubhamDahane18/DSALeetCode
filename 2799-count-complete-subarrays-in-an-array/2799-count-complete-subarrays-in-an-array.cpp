class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int n = nums.size();
        int l = 0;
        int r = 0;
        unordered_map<int, int> mpp;
        unordered_set<int> st;
        int ans = 0;

        for(int num: nums){
            st.insert(num);
        }

        while(r < n){
            mpp[nums[r]]++;

            while(mpp.size() == st.size()){
                ans += n - r;
                mpp[nums[l]]--;

                if(mpp[nums[l]] == 0){
                    mpp.erase(nums[l]);
                }

                l++;
            }

            r++;
        }

        return ans;
    }
};