class Solution {
public:
string mergeAlternately(string word1, string word2) {
auto it1 = word1.begin();
auto it2 = word2.begin();

    string s = "";

    while (it1 != word1.end() || it2 != word2.end()) {

        if (it1 != word1.end()) {
            s += *it1;
            ++it1;
        }

        if (it2 != word2.end()) {
            s += *it2;
            ++it2;
        }
    }

    return s;
}

};