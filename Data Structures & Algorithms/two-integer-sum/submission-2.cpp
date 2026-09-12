class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> check; // maps: number -> its index

        for (int i = 0; i < nums.size(); i++) {
            int difference = target - nums[i];

            // Look for the complement in our map
            if (auto value = check.find(difference); value != check.end()) {
                // Found it! Return the indices directly using an initializer list {}
                return {value->second, i}; 
            }

            // If not found, log the current number and its index into the map
            check[nums[i]] = i;
        }

        return {}; // Return empty vector if no solution exists (to satisfy compiler)
    }
};

// create set from nums
// do target - nums[i] to get difference and check if set contains that
// if set contains, 
// if (nums[i] <= difference){ return vector<nums[i] and difference }
// else { return vector<difference, nums[i]; }