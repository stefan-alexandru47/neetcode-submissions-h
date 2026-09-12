#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Keeps track of: [ Number -> Its Index ]
        std::unordered_map<int, int> check;
        
        for (int i = 0; i < nums.size(); ++i) {
            int difference = target - nums[i];
            
            // 1. INIT: Search the map on the heap and store the iterator reference
            // 2. CONDITION: Ensure it's not pointing to the 'out-of-bounds' boundary marker
            if (auto value = check.find(difference); value != check.end()) {
                
                // FOUND! Unpack the iterator using arrow syntax 
                // value->second gets the index of the matching number stored in the map
                return {value->second, i}; 
            }
            
            // NOT FOUND: Add the current number and its index to the map
            check[nums[i]] = i;
        }
        
        // Return an empty vector if no solution exists (required by syntax)
        return {};
    }
};