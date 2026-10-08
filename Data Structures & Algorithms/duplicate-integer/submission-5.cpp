#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // using a hashMap to maintain the recorded elements
        unordered_map<int, int> check;
        int i;
        for (i = 0; i < nums.size(); i++) {
            check[nums[i]] += 1;
            if (check[nums[i]] > 1) {
                return true;
            }
        }
        return false;
    }
};
