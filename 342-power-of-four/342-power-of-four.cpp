class Solution {
public:
    bool isPowerOfFour(double n) {
        if (n == 1){
            return true;
        }
        else if (n < 1){
            return false;
        }
        else{
            return isPowerOfFour(n / 4.0);
        }
    }
};
// if n == 1:
//     return True
// elif n < 1:
//     return False
// else:
//     return self.isPowerOfFour(n/4)
// // if n == 1:
// //             return True
// //         elif n < 1:
// //             return False
// //         else:
// //             return self.isPowerOfFour(n/4)