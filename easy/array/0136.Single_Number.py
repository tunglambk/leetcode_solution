class Solution:
    # https://leetcode.com/problems/single-number/discuss/558767/Python-Space-O(1)-XOR%2BReduce-Very-Simple-One-Liner-(With-Explanation)
    # Explain:
    # nums = [2,4,5,4,3,5,2]
    # XORing everything together
    # = 2 ^ 4 ^ 5 ^ 4 ^ 3 ^ 5 ^ 2
    # = (2^2) ^ (4^4) ^ (5^5) ^ 3
    # = 0 ^ 0 ^0 ^ 3
    # = 3
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)
