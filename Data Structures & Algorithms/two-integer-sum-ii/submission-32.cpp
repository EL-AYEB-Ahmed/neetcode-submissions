#include <vector>
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        auto beg = numbers.begin();
        auto end = numbers.end()-1;
        int i = 0;
        int j = numbers.size() -1;
        while  (*beg + *end != target ){
            if (*beg + *end < target){
                ++i;
                ++beg;
            }
            else if (*beg + *end > target){
                --j;
                --end;
            }
        }
        return {i+1 , j+1};
    }
};
