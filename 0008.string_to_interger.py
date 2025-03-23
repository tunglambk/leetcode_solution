class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        if s[0].isdigit():
            sign = 1
            i = 0
        elif s[0] == "+":
            sign = 1
            i = 1
        elif s[0]=="-":
            sign = -1
            i = 1
        else:
            return 0

        valid_num = ""
        while i < len(s):
            if s[i].isdigit():
                valid_num += s[i]
            else:
                break
            i += 1
        if not valid_num:
            return 0
        
        product_num = 1
        res = int(valid_num)

        res *= sign
        pos_threshold = pow(2,31)-1
        neg_threshold = -pow(2,31)

        if res > pos_threshold:
            return pos_threshold
        elif res < neg_threshold:
            return neg_threshold
        return res
        
