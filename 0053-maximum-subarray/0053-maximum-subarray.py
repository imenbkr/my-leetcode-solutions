class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #initialize maximum sub array
        max_sub_arr = nums[0]
        #initialize current sum
        curr_sum = 0
        
        #loop over array
        for n in nums :
            #sliding window
            if curr_sum <0 :
                curr_sum =0
            curr_sum+= n
            max_sub_arr = max(max_sub_arr, curr_sum)
            
        return max_sub_arr