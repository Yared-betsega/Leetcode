class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1){
            return 0;
        }
        int maxReach = nums[0];
        int steps = 1;
        int i = 0;
        while (i < nums.size()){
            if (maxReach >= nums.size() - 1){
                return steps;
            }
            int temp = 0;
            while (i < nums.size() && i <= maxReach){
                temp = max(temp, i + nums[i]);
                i++;
            }
            maxReach = temp;
            steps++;
        }
        return steps;
    }
};


// # Single loop O(n) Solution
// if len(nums) == 1:
//     return 0
// maxReach, steps = nums[0], 1
// i = 0
// while i < len(nums):
//     if maxReach >= len(nums) - 1:
//         return steps
//     temp = 0
//     while i < len(nums) and i <= maxReach:
//         temp = max(temp, i + nums[i])
//         i += 1
//     maxReach = temp
//     steps += 1
// return steps