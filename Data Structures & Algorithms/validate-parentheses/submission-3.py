class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for this in s:
            if this in pairs:
                if stack and stack[-1] == pairs[this]:
                    stack.pop()
                else: return False
            else: stack.append(this)
        
        if not stack:
            return True
        else: return False
                    




# push opening brackets onto stack
# for closing brackets, check if corresponding opening bracket is at the top of the stack
# remove the corresponding opening bracket
# this opens up any other corresponding opening brackets
# if corresponding bracket isn't found, return false

# by the end, all brackets are removed and you have confirmed the string is correct
# return true if stack is empty