class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        clean_text = re.sub("[^a-zA-Z\s]", " ", paragraph)
        clean_text = clean_text.lower()
        word_list = clean_text.split()
        count_dict = dict()

        for word in word_list:
            if word in count_dict:
                count_dict[word] += 1
            else:
                count_dict[word] = 0

        count_list = list(sorted(count_dict.items(), key=lambda item: -item[1]))

        for candi, freq in count_list:
            if candi not in banned:
                return candi