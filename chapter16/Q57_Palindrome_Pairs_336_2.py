# Answer2
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_dict = {word: i for i, word in enumerate(words)}
        result = []

        for index, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):  # 모든 가능한 분할 지점
                prefix, suffix = word[:j], word[j:]

                # 1. suffix가 팰린드롬이고, prefix의 역순이 단어 리스트에 존재하는 경우
                if suffix == suffix[::-1] and prefix[::-1] in word_dict:
                    pair_index = word_dict[prefix[::-1]]
                    if pair_index != index:
                        result.append([index, pair_index])

                # 2. prefix가 팰린드롬이고, suffix의 역순이 단어 리스트에 존재하는 경우
                # (j > 0은 중복 방지: 빈 문자열이 고려될 경우 중복 발생 가능)
                if j > 0 and prefix == prefix[::-1] and suffix[::-1] in word_dict:
                    pair_index = word_dict[suffix[::-1]]
                    if pair_index != index:
                        result.append([pair_index, index])

        return result