class Solution:
    # https://leetcode.com/problems/longest-palindromic-substring/solution/
    
    def expandAroundCenter(self, s, left, right):
        while (left>=0) and (right<len(s)) and (s[left] == s[right]):
            left = left - 1
            right = right + 1
        return right - left - 1
        
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        str_len = len(s)
        
        if (s == None) or (str_len < 1):
            return ""
        
        start = 0
        end = 0
        
        for i in range(str_len):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            
            lenght = max(len1, len2)
            
            if(lenght > end-start):
                start = i - (lenght-1)//2
                end = i+ lenght//2
        return s[start:end+1]
