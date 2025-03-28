class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for item in s:
            if item != "#":
                stack1.append(item)
            elif stack1:
                stack1.pop()
        for item in t:
            if item != "#":
                stack2.append(item)
            elif stack2:
                stack2.pop()
        return stack1 == stack2
        
