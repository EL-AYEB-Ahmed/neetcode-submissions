class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        auto it1 = word1.begin();
        int i = 0;
        auto it2 = word2.begin();
        string s = "";
        while ( i<word1.size() && i < word2.size() ){
            s+= *it1 ;
            s+= *it2;
            ++it1;
            ++it2;
            ++i;
        }
        if (i==word1.size()){
            return s + word2.substr(i);
        }
        else if (i==word2.size()){
            return s + word1.substr(i);
        }
        else return s;
    }
};