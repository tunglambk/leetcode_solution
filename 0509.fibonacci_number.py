class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f_n_1 = 1
        f_n_2 = 0
        if n < 2:
            return n
        for i in range(2, n+1):
            fn = f_n_2 + f_n_1
            f_n_2 = f_n_1
            f_n_1 = fn
        return fn
