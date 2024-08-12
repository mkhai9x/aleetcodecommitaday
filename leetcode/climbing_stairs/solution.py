class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        dp = [1] * (n + 1)  # dp[i] represent number of way to get to position ith
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


print(Solution().climbStairs(2))
