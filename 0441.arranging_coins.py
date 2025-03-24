class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        ret = 0
        while low <= high:
            mid = (low + high) // 2
            if (mid * (mid + 1)) // 2 <= n:
                low = mid + 1
            else:
                high = mid - 1
        return low - 1
