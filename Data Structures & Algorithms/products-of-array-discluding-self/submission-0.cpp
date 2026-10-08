class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prods;
        for (int i = 0; i < nums.size(); i++) {
            prods.push_back(1);
            for (int j = 0; j < nums.size(); j++) {
                if (i == j) continue;
                prods[i] *= nums[j];
            }
        }
        return prods;
    }
};
