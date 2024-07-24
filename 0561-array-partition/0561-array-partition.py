class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sorted_nums = sorted(nums)
        res= 0
        
        for i in range(0, len(sorted_nums), 2):
            res+=sorted_nums[i]
            
        return res
        