# My solution1
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        seq = [0, 1]
        for _ in range(n - 1):
            seq.append(seq[-1] + seq[-2])
        return seq[-1]