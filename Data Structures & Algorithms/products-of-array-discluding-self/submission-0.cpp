class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int pro = 1;
        int zero = 0;
        vector<int> prod;

        for (int i : nums) {
            if (i != 0)
                pro *= i;
            else
                zero++;
        }

        for (int i : nums) {
            if (zero == 0) {
                prod.push_back(pro / i);
            } else if (zero == 1) {
                prod.push_back(i == 0 ? pro : 0);
            } else {
                prod.push_back(0);
            }
        }

        return prod;
    }
};
