# Answer
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            for task, _ in counts.most_common(n + 1):
                sub_count += 1
                result += 1
                counts.subtract(task)
                counts += collections.Counter()  # 0 이하인 아이템 제거
            if not counts:
                break
            result += n - sub_count + 1

        return result