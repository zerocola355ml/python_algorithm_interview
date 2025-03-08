# My solution4
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks).values()
        max_freq = max(freq)
        num_of_max_freq = list(freq).count(max_freq)
        return max((n + 1) * (max_freq - 1) + num_of_max_freq, len(tasks))
