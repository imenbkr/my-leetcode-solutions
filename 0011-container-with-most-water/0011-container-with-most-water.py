class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start =0
        end = len(height)-1
        step = 0
        max_water = 0
        
        while(start < end):
            step = end - start
            min_x = min(height[start], height[end])
            max_water = max(max_water, (step*min_x))
           
            if height[start] < height[end]:
                start+=1
            else:
                end-=1
    
        return max_water
            