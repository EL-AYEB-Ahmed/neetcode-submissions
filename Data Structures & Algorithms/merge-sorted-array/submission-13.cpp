class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

        auto it1 = nums1.begin();
        auto it2 = nums2.begin();

        for (int i = 0; i < m && it2 != nums2.end(); ++i) {

            if (*it1 > *it2) {
                it1 = nums1.insert(it1, *it2);
                ++it2;
                ++it1;
                ++m;
            }
            else {
                ++it1;
            }
        }

        while (it2 != nums2.end()) {
            nums1.insert(nums1.begin() + m, *it2);
            ++it2;
            ++m;
        }

        nums1.resize(m);
    }
};