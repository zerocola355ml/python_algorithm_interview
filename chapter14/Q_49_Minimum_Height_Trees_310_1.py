# My solution
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        max_degree = -float("inf")
        degree_vertex = collections.defaultdict(set)
        graph = collections.defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        for x in graph:
            degree = len(graph[x])
            degree_vertex[degree].add(x)
            max_degree = max(max_degree, degree)

        while len(degree_vertex) > 1:
            for v in list(degree_vertex[1]):
                degree_vertex[1].remove(v)
                nei = graph[v].pop()
                nei_degree = len(graph[nei])
                degree_vertex[nei_degree].remove(nei)
                if not degree_vertex[nei_degree]:
                    del degree_vertex[nei_degree]
                degree_vertex[nei_degree - 1].add(nei)
                graph[nei].remove(v)
                max_degree = min(max_degree, nei_degree - 1)

        return list(degree_vertex[max_degree])