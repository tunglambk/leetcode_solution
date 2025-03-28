class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ""
        for pos in range(len(strs[0])):
            flag = True
            for string in strs[1:]:
                if len(string) < pos + 1:
                    flag = False
                    break
                if string[pos] != strs[0][pos]:
                    flag = False
                    break
            if flag:
                common_prefix += strs[0][pos]
            else:
                break
        return common_prefix
        
