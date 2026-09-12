class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        j = 0
        window, countT = Counter(), Counter()

        res, resLen = [-1, -1], float('inf')
        l = 0

        for c in t: # add freqs to countT
            countT[c] += 1

        have, need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            
            if c in countT and window[c] == countT[c]: # check if freqs match, if they do we have 1+ 
                have += 1

            while have == need: # while condition is met
                if (r - l + 1) < resLen: # append res indices and their len
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1 # move l pointer and remove its frequency
                if s[l] in countT and window[s[l]] < countT[s[l]]: # 
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""