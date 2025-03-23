class Solution(object):
    
    def next(self, n):
        res = 0
        while n > 0:
            digit = n%10
            res += digit**2
            n //= 10
        return res

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        def isHappy(n, seen):
            if n==1:
                return True
            next_num = self.next(n)
            if next_num in seen:
                return False
            seen.add(next_num)
        
            return isHappy(next_num, seen)
        return isHappy(n, seen)
