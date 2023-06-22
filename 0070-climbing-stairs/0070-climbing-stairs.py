class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp= {}
        #no step
        dp[0]=0
        #one step
        dp[1]=1
        #ywo steps
        dp[2]=2
        
        if (n==0):
            return dp[0]
        if (n==1):
            return dp[1]
        
        for i in range(3, n+1):
            #for n > 2 : F(n) = F(n-1) + F(n-2) (size of previous steps)
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
            