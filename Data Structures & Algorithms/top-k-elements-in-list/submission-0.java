class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<List<Integer>> icebuckets = new ArrayList<>();
        Map<Integer, Integer> frequencies = new HashMap<>();

        for (int num : nums) {
            frequencies.put(num, frequencies.getOrDefault(num, 0) + 1);
        }

        int maxFreq = Collections.max(frequencies.values()); //determine max frequency to size buckets

        for (int i = 0; i <= maxFreq; i++) { // changed to include max freq
            icebuckets.add(new ArrayList<>());
        }

        for (int num : frequencies.keySet()) {
            int freq = frequencies.get(num);
            icebuckets.get(freq).add(num);
        }

        int[] topK = new int[k];
        int count = 0; // add count to keep count of topK

        for (int i = icebuckets.size() - 1; i >= 0 && count < k; i--){
            List<Integer> bucket = icebuckets.get(i); // assign buckets to list var to avoid empty buckets
            for (int j = 0; j < bucket.size() && count < k; j++){
                topK[count] = bucket.get(j);
                count++; // increase count
            }
        }
        return topK;
    }
} // took 3 hours to solve, got stuck on logic and gpt helped

// make hash map with key being number in list and value being integer
// go thru each element
// add element as key if it isn't there already + increment key integer value
// return 

// make hashmap of 6 keys with arraylist value
// each key is a frequency
// count how many times each value occurs, add them to respective frequency in map
// to get top K, go from 6 to 1 buckets, and get first 2 values 