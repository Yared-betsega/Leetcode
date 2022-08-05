class Solution {
public:
    int climbStairs(int n) {
        int oneStep = 1;
        int twoStep = 1;
        if (n < 2){
            return 1;
        }
        for(int i = 2; i <= n; i++){
            int temp = oneStep + twoStep;
            oneStep = twoStep;
            twoStep = temp;
        }
        return twoStep;
    }
};
