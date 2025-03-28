class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hash_map = dict()
        for item in nums:
            if item in hash_map:
                hash_map[item]+=1
            else:
                hash_map[item]=1
        sum = 0
        for k, v in hash_map.items():
            if v == 1:
                sum+=k
        return sum
