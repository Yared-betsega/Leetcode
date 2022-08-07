class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        for (int i = 1; i < nums.size(); i++){
            nums[i] = max(nums[i] + nums[i - 1], nums[i]);
        }
        int m = nums[0];
        for (int i = 1; i < nums.size(); i++){
            m = max(m, nums[i]);
        } 
        return m;
    }
};

// # time and space complexity
// # time: O(n)
// # space: O(1)