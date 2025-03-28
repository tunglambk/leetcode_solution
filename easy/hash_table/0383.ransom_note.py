class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        count_rsn = dict()
        count_mgz = dict()
        for c in ransomNote:
            if c not in count_rsn:
                count_rsn[c] = 1
            else:
                count_rsn[c] += 1
        
        for c in magazine:
            if c not in count_mgz:
                count_mgz[c] = 1
            else:
                count_mgz[c] += 1
        
        for k in count_rsn:
            if k not in count_mgz or count_mgz[k] < count_rsn[k]:
                return False
        return True
        '''

        for char in ransomNote:
            if char not in magazine:
                return False
            magazine = magazine.replace(char, '', 1) 
        return True
