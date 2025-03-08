# My solution
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        result = [0] * len(people)

        while people:
            height, front = people.pop()
            idx = 0
            temp = front
            while temp > 0:
                if result[idx] == 0:
                    temp -= 1
                idx += 1
            while result[idx] != 0:
                idx += 1
            result[idx] = [height, front]

        return result