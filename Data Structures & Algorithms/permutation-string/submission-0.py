from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter()

        for i in range(len(s1)):
            s1_freq[s1[i]] += 1

        s2_freq = Counter()

        i = 0
        l = 0

        for i in range(len(s2)):
            s2_freq[s2[i]] += 1

            while i - l + 1 > len(s1):
                s2_freq[s2[l]] -= 1
                l += 1

            if s1_freq == s2_freq and (i - l + 1) == len(s1):
                return True

        return False

# s1 = "abc"
# s2 = "lecacb"

# move right pointer and add freqs
# evaluate if move l pointer
            