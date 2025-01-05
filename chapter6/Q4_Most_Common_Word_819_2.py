class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cleaned = re.sub(r"[^a-z\s]", " ", paragraph.lower())
        for word in dict(sorted(collections.Counter(cleaned.split()).items(), key = lambda item: item[1], reverse = True)):
            if word not in banned:
                return word