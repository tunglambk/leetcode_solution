class Solution:
    # Time Limit Exceeded
    #def maxArea(self, height: List[int]) -> int:
    #    max_area = 0
        
    #    for i in range(len(height)-1):
    #        for j in range(i+1, len(height)):
    #            l = j - i
    #            h = min(height[i], height[j])
    #            area = l * h
    #            if area > max_area:
    #                max_area = area
    #    return max_area
    
    def maxArea(self, height: List[int]) -> int:
        
        max_area = 0
        
        head = 0
        tail = len(height)-1
        
        while head != tail:

            if height[tail] < height[head]:
                area = abs(tail-head) * height[tail]
                tail -= 1
            else:
                area = abs(tail-head) * height[head]
                head += 1
                
            if area > max_area:
                max_area = area
                
        return max_area
