class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dif = new HashMap<>();
        int[] result = new int[2];
        int i = 0;

        for (int num : nums) {
            if (dif.containsKey(target - num)) {
                result[0] = dif.getOrDefault(target - num, 0);
                result[1] = i;
                return result;
            }
            dif.put(num, i);
            i++;
        }
        return result;
    }
}

// le brute = adding each element and comparing to target (bad)

// le good solve = trec prin fiecare numar si ii salvez diferenta intr-un hashset, 
// dupa trec prin fiecare numar din nou si vad daca contains diferenta in hashset

