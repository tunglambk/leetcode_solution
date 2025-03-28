class Solution:
    def _relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = {num: 0 for num in arr2}
        
        remain = []
        for num in arr1:
            if num in counts:
                counts[num] += 1
            else:
                remain.append(num)
        
        result = []
        for num in arr2:
            result.extend([num] * counts[num])
        
        result.extend(sorted(remain))
        return result
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_index = {num: i for i, num in enumerate(arr2)}
        
        def sort_key(x):
            return (0, arr2_index[x]) if x in arr2_index else (1, x)
        
        return sorted(arr1, key=sort_key)
