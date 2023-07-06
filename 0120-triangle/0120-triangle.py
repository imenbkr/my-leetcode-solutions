class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #constraints :
        if len(triangle) < 1 or len(triangle) > 200:
            return 0
        
        dp= [0]*(len(triangle[-1])+1 )
        
        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n+min(dp[i], dp[i+1])
        
        return dp[0]