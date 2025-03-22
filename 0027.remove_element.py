class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        length = len(nums)
        i = 0
        j = length - 1
        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i] = nums[j]
                    i += 1
                j -= 1
                count += 1
            else:
                i+= 1
        return length - count       
