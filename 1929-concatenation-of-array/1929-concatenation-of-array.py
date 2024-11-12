class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = [0]*2*len(nums)

        j=0
        while(j < len(ans)):
            for i in range(len(nums)):
                ans[j] = nums[i]
                j+=1


        return ans
