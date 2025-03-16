# Answer1
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isnumeric():
            return [int(expression)]

        def operation(left, right, operator):
            output = []
            for l in left:
                for r in right:
                    output.append(eval(str(l) + operator + str(r)))
            return output

        result = []
        for i, char in enumerate(expression):
            if char in '+-*':
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                result.extend(operation(left, right, char))

        return result