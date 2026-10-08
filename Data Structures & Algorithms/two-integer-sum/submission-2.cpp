#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> rec; // val -> index

        int nums_size = nums.size();
        int i;
        for (i = 0; i < nums_size; i++) {
            rec[nums[i]] = i;
        }

        for (i = 0; i < nums_size; i++) {
            int diff = target - nums[i];
            if (rec.count(diff) == 1 && rec[diff] != i) {
                return {i, rec[diff]};
            }
        }
        return {};
    }
};
