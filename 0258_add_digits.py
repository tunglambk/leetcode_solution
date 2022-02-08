class Solution(object):
    def old_addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        sum = num
        while len(num_str) > 1:
            sum = 0
            for c in num_str:
                sum += int(c)
            num_str = str(sum)
        return sum
    
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # https: // en.wikipedia.org / wiki / Digital_root
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
