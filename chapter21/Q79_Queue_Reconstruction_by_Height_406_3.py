# Answer2
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        result = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))

        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result