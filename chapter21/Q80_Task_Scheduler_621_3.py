# My solution3
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        max_freq = counts.most_common(1)[0][1]
        max_char = [key for key, val in counts.items() if val == max_freq]
        return max((n + 1) * (max_freq - 1) + len(max_char), len(tasks))