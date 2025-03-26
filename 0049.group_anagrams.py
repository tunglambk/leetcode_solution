class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = dict()
        for item in strs:
            sorted_str = ''.join(sorted(item))

            if sorted_str not in anagrams_map:
                anagrams_map[sorted_str] = [item]
            else:
                anagrams_map[sorted_str].append(item)
        
        return list(anagrams_map.values())

