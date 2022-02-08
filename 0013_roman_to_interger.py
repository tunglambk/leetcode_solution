class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        total = 0
        pre_num = 0
        
        for char in s:
            current_num = roman_int[char]
            total += current_num
            
            if current_num > pre_num:
                total -= 2*pre_num
            pre_num = current_num
        return total
            
