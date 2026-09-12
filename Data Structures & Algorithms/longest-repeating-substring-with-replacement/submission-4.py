from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = Counter() 
        maxf = 0

        res = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            maxf = max(maxf, freq[s[r]])
        
            while r - l + 1 - maxf > k:
                freq[s[l]] -= 1
                l += 1

            res = r - l + 1
        return res

