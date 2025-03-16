# Answer5
class Solution:
    def isOperator(self, ch):
        return ch == '+' or ch == '-' or ch == '*'

    def getDiffWays(self, i, j, dp, expression):
        if (i, j) in dp:
            return dp[(i, j)]

        len_substring = j - i + 1
        if len_substring <= 2:
            result = [int(expression[i:j+1])]
            dp[(i, j)] = result
            return result

        res = []
        for ind in range(i, j + 1):
            if self.isOperator(expression[ind]):
                op = expression[ind]

                left = self.getDiffWays(i, ind - 1, dp, expression)
                right = self.getDiffWays(ind + 1, j, dp, expression)

                for l in left:
                    for r in right:
                        if op == '+':
                            res.append(l + r)
                        elif op == '-':
                            res.append(l - r)
                        elif op == '*':
                            res.append(l * r)

        dp[(i, j)] = res
        return res

    def diffWaysToCompute(self, expression: str):
        dp = {}
        return self.getDiffWays(0, len(expression) - 1, dp, expression)