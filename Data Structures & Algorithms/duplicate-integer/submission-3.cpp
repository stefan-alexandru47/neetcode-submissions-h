class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        unordered_set<int> items;
        for (int i = 0; i < nums.size(); i++){
            int currNum = nums[i]; 
            if (items.contains(currNum)){
                return true;
            }
            items.insert(currNum);
        }
        return false;
    }
};