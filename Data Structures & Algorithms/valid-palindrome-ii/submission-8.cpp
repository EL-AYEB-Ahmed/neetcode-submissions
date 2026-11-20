#include <string>
using namespace std;

class Solution {
public:
    bool palindrom(string s) {
        int i = 0;
        int j = s.size() - 1;

        while (i < j) {
            if (s[i] != s[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    bool validPalindrome(string s) {
        int i = 0;
        int j = s.size() - 1;

        while (i < j) {
            if (s[i] != s[j]) {
                return palindrom(s.substr(0, i) + s.substr(i + 1)) ||
                       palindrom(s.substr(0, j) + s.substr(j + 1));
            }
            i++;
            j--;
        }

        return true;
    }
};