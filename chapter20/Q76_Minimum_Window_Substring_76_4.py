# Answer3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)  # 필요한 문자 개수
        missing = len(t)  # 남은 필요 문자 개수
        left = start = end = 0

        for right, char in enumerate(s, 1):  # right는 1부터 시작 (슬라이싱 편의)
            if need[char] > 0:
                missing -= 1
            need[char] -= 1  # 윈도우에 포함된 문자 수 감소

            if missing == 0:  # 모든 문자가 포함됨
                while need[s[left]] < 0:  # 불필요한 문자 제거
                    need[s[left]] += 1
                    left += 1

                if end == 0 or right - left < end - start:  # 최소 길이 갱신
                    start, end = left, right

                need[s[left]] += 1  # left 증가로 인해 한 문자 제거됨
                missing += 1
                left += 1

        return s[start:end]
