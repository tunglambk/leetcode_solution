class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        open = set(["(", "{", "["])

        stack = []
        for item in s:
            if item in open:
                stack.append(item)
            elif len(stack) == 0:
                return False   
            else:
                if pair[item] != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True  
