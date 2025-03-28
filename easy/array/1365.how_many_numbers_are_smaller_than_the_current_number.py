class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = dict()
        max_num = 0
        for item in nums:
            if item not in counts:
                counts[item] = 1
            else:
                counts[item] += 1
            max_num = max(max_num, item)
        
        count_less = {0: 0}
        for item in range(1, max_num+1):
            count_less[item] = count_less[item-1] + counts.get(item-1, 0)
        
        return [count_less[item] for item in nums]
