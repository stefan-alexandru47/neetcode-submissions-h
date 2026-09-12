class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        list2 = []
        # in python, strings are basically lists of chars
        clean_s = "".join([char.lower() for char in s if char.isalnum()]) # shorthand for making letter-only str
        # loops through each char in string s and returns it to temporary list[] (the return is the first keyword's value, so you can modify its return)
        # join without anything in between 
        y = -1

        # for the backwards pointer, make it start at -1 and decrement
        # forwards pointer is i, and no need to manually increment it

        for i in range(len(clean_s)):
            if i >= len(clean_s)//2: # while half of the string is not reached
                break
            list1.append(clean_s[i])
            list2.append(clean_s[y])
            y -= 1
            
        return list1 == list2

# use two pointers

# have two data structs
# have a loop that makes one pointer go from index 1 forward and one that goes from -1 
# have the loop stop when half of the length is reached 
# for each letter the pointer sees, save it in the data struct 
# see if data structs are equal