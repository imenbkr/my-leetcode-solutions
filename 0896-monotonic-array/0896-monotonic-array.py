class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
      
        if (nums[-1] - nums[0]) <0:
            nums.reverse()
        
        for i in range(len(nums)-1):
            if not (nums[i] <= nums[i+1]):
                return False
            
        return True
        
        