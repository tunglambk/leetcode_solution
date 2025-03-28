class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums)//2 - 1
        ret = len(nums) - 1
        while low <= high:
            mid = int((low+high)//2)
            if nums[mid*2] != nums[mid*2+1]:
                high = mid - 1
                ret = 2*mid
            else:
                low = mid + 1
        return nums[ret]
