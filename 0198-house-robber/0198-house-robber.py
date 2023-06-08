class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))

        
        for i in range(2, len(nums)):
            #we either take current house + max of robbed houses (i-2) : non adjacents
            #or skip current house and take robbed house (i-1) so its non adjacent
            dp.append(max(nums[i] + dp[i-2], dp[i-1]))

        return dp[-1]