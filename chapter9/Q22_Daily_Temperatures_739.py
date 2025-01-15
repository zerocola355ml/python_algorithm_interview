class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                day = stack.pop()
                result[day] = index - day
            stack.append(index)

        return result