# Answer
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                nei = graph[leaf].pop()
                graph[nei].remove(leaf)
                if len(graph[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves

        return leaves