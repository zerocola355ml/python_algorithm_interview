# Answer6
class Solution:
    def isOperator(self, ch):
        return ch == '+' or ch == '-' or ch == '*'

    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        dp = [[[] for _ in range(n)] for _ in range(n)]

        def isValidExpression(i, j):
            return (i == 0 or self.isOperator(expression[i - 1])) and (j == n - 1 or self.isOperator(expression[j + 1]))

        for i in range(n):
            if isValidExpression(i, i):
                dp[i][i] = [int(expression[i])]

        for i in range(n - 1):
            if isValidExpression(i, i + 1):
                dp[i][i + 1] = [int(expression[i:i + 2])]

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if not isValidExpression(i, j):
                    continue

                dp[i][j] = []
                for ind in range(i, j + 1):
                    if self.isOperator(expression[ind]):
                        op = expression[ind]

                        left = dp[i][ind - 1]
                        right = dp[ind + 1][j]

                        for l in left:
                            for r in right:
                                if op == '+':
                                    dp[i][j].append(l + r)
                                elif op == '-':
                                    dp[i][j].append(l - r)
                                elif op == '*':
                                    dp[i][j].append(l * r)

        return dp[0][n - 1]