# My solution2
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        result = 0

        while counts:
            cycle = n + 1
            while cycle:
                for char, freq in counts.most_common():
                    counts[char] -= 1
                    cycle -= 1
                    result += 1
                    if counts[char] == 0:
                        del counts[char]
                    if cycle == 0:
                        break
                if counts:
                    result += cycle
                cycle = 0
        return result