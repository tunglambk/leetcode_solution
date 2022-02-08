class Solution(object):
    def _twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_1, num in enumerate(nums):
            require = target - num
            if require in nums:
                index_2 = nums.index(require)
                if index_2 != index_1:
                    break
        return [index_1, index_2]
    
    def twoSum(self, nums, target):
        # two point
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1
