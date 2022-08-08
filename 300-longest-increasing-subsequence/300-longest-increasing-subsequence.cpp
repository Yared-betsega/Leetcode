class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        for (int i = 1; i < nums.size(); i++){
            for (int j = 0; j < i; j++){
                if (nums[i] > nums[j]){
                    dp[i] = max(dp[j] + 1, dp[i]);
                }
            }
        }
        int ans = 0;
        for (int x: dp){
            ans = max(x, ans);
        }
        return ans;
    }
};