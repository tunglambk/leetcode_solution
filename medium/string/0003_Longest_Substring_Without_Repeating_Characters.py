class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_len = len(s)
        ret = 0
        
        mapping_dict = dict()
        
        i = 0
        
        for j in range(str_len):
            if s[j] in mapping_dict:
                i = max(i, mapping_dict[s[j]])
            
            ret = max(ret, j-i+1)
            mapping_dict[s[j]] = j + 1
        
        return ret
