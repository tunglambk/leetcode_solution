class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        results = [[1], [1,1]]
        if numRows < 2:
            return results[:numRows]
        for i in range(2, numRows):
            next_row = [1] * (i+1)
            for j in range(1, i):
                next_row[j] = results[i-1][j-1] + results[i-1][j]
            results.append(next_row)
        return results
        
