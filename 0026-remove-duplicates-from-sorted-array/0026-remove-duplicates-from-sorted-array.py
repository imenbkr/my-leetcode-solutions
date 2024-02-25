class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = [nums[0]]  
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] not in new_nums:
                new_nums.append(nums[i])
        
     
        nums[:] = new_nums[:] # updating nums to contain the unique elements
        #source : https://sparkbyexamples.com/python/update-list-element-in-python/
        
        return len(new_nums)
