# Answer2
class Solution:
    dp = collections.defaultdict(int)
    dp[1] = 1
    def fib(self, n: int) -> int:
        for i in range(2, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[n]