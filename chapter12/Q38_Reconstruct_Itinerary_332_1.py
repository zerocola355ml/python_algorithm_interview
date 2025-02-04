# Answer1
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def helper(start):
            while graph[start]:
                helper(graph[start].pop())
            route.append(start)

        helper('JFK')
        return route[::-1]