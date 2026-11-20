#include <string>
class Solution {
public:
    bool palindrom(string s){
        auto beg = s.begin();
        auto end = s.end()-1;
        bool res = true;
        while (beg < end && res){
            if (*beg!=*end){
                res = false;
            }
            ++beg;
            --end;
        }
        return res;
    }
    bool validPalindrome(string s) {
        auto b = s.begin();
        int i = 0;
        auto e = s.end()-1;
        int j = s.size() -1;
        bool r = true;
        while ((b < e) && r){
            if(*b != *e){
                return palindrom(s.substr(0,i) + s.substr(i+1)) || 
                       palindrom(s.substr(0,j) + s.substr(j+1)) ;
            }
            ++b;
            --e;
            ++i;
            --j;
        }       
        return r;
    }
};