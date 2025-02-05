# Answer2
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        trace = set()
        visited = set()

        for a, b in prerequisites:
            graph[a].append(b)

        def has_cycle(course):
            if course in trace:
                return True
            if course in visited:
                return False
            trace.add(course)
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
                # 오답1. return has_cycle(neighbor) 하면 안됨.
            trace.remove(course)
            visited.add(course)
            return False

        for course in list(graph):  # 오답2. 그냥 graph로 에러 발생.
            if has_cycle(course):
                return False

        return True