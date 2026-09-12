class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean_s = "".join([char.lower() for char in s if char.isalnum()])
        y = -1

        for i in range(len(clean_s)):
            if i >= len(clean_s)//2: # while half of the string is not reached
                break
            if clean_s[i] != clean_s[y]:
                return False
            y -= 1
            
        return True
