class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        int n = nums.size();
        int l = 0;
        int r = 0;
        long long score = 0;
        long long ans = 0;
        long long sum = 0;

        while(r < n){
            sum += nums[r];
            score = sum * (r - l + 1);

            while(score >= k){
                sum -= nums[l];
                l++;
                score = sum * (r - l + 1);
            }
            ans += (r - l + 1);
            r++;
        }

        return ans;
    }
};