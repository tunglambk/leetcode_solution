class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 0 or numRows == 1:
            return s
        
        num_char = len(s)
        
        if num_char == 0 or num_char == 1:
            return s

        result = [""] * numRows
        
        # The number of characters in a zigzac
        period = 2 * (numRows -1)
        
        for i in range(num_char):
            row = i % period
            
            if row >= period//2:
                row = period - row
            
            result[row] += s[i]
            
        return "".join(result)
