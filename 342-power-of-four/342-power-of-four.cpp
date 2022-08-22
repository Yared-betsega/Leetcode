class Solution {
public:
    bool isPowerOfFour(int n) {
        if (n == 1){
            return true;
        }
        else if (n % 4 != 0 || n < 1){
            return false;
        }
        else{
            return isPowerOfFour(n / 4);
        }
    }
};
