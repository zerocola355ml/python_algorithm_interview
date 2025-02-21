# Answer3
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        unique_length = set(len(word) for word in words)
        inverse_word_dict = {word[::-1]: i for i, word in enumerate(words)}

        output = []

        for i, word in enumerate(words):
            l = len(word)
            if l == 0:
                continue

            if word != word[::-1] and word in inverse_word_dict:
                output.append([i, inverse_word_dict[word]])

            for j in range(1, l + 1):
                if l - j in unique_length:
                    if word[:j] == word[(j - 1)::-1] and word[j:] in inverse_word_dict:
                        output.append([inverse_word_dict[word[j:]], i])
                    if word[-j:] == word[:-(j + 1):-1] and word[:-j] in inverse_word_dict:
                        output.append([i, inverse_word_dict[word[:-j]]])

        return output