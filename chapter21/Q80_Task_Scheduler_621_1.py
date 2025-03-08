# My solution1
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        cooling = collections.defaultdict(lambda: -n - 1)
        counts = collections.Counter(tasks)
        remain = len(tasks)

        while remain > 0:
            idle = True
            for task in counts.most_common():
                if result - cooling[task[0]] <= n or counts[task[0]] == 0:
                    continue
                else:
                    counts[task[0]] -= 1
                    cooling[task[0]] = result
                    result += 1
                    remain -= 1
                    idle = False
                    break
            if idle:
                result += 1
        return result
