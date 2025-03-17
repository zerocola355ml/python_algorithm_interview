# Answer1
class Solution:
    memo = collections.defaultdict(int) # memo를 fib 안에서 정의하면 느리다.
    memo[0] = 0
    memo[1] = 1
    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        return self.fib(n - 1) + self.fib(n - 2)