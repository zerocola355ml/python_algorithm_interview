# Answer1
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)  # b -> a

        visited = [0] * numCourses  # 0: 방문 안 함, 1: 방문 중, 2: 방문 완료

        def has_cycle(course):
            if visited[course] == 1:  # 사이클 발견
                return True
            if visited[course] == 2:  # 이미 방문 완료
                return False

            visited[course] = 1  # 현재 방문 중 표시
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            visited[course] = 2  # 방문 완료 표시
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True