class Solution:
    def reverse(self, x: int) -> int:
    
        x_str = str(x)
        rev_str = ''
        if x >= 0:
            rev_str = x_str[::-1]
        else:
            rev_str = '-'
            rev_str += x_str[1:][::-1]
        
        rev_num = int(rev_str)
        if rev_num >= (2**31-1) or rev_num <= (-2**31):
            return 0
        return rev_num
