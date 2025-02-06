# Answer2
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for vertex, neighbor, time in times:
            graph[vertex].append((neighbor, time))

        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            time, vertex = heapq.heappop(Q)
            if vertex not in dist:
                dist[vertex] = time
                if len(dist) == n:  # 여기로 옮기면 더 빨라진다.
                    return max(dist.values())
                for neighbor, delta in graph[vertex]:
                    heapq.heappush(Q, (time + delta, neighbor))

        return -1




