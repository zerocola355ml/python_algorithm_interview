# My solution
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        memo = {2:0, 3:0, 4:0}
        curr = 0
        for num in data:
            if num // (2 ** 7) == 0: # 0xxxxxxx
                if memo[2] > 0 or memo[3] > 0 or memo[4] > 0:
                    return False
                continue
            else: # 1xxxxxxx
                num = num % (2 ** 7)
                if num // (2 ** 6) == 0: # 10xxxxxx
                    if curr == 0:
                        return False
                    else:
                        memo[curr] += 1
                        if memo[curr] == curr:
                            memo[curr] = 0
                            curr = 0
                else: ## 11xxxxxx
                    num = num % (2 ** 6)
                    if num //(2 ** 5) == 0: # 110xxxxx
                        if curr == 0:
                            memo[2] = 1
                            curr = 2
                        else:
                            return False
                    else: # 111xxxxx
                        num = num % (2 ** 5)
                        if num // (2 ** 4) == 0: # 1110xxxx
                            if curr == 0:
                                memo[3] = 1
                                curr = 3
                            else:
                                return False
                        else: # 1111xxxx
                            num = num % (2 ** 4)
                            if num // (2 ** 3) == 0: # 11110xxx
                                if curr == 0:
                                    memo[4] = 1
                                    curr = 4
                                else:
                                    return False
                            else:
                                return False
        if memo[2] > 0 or memo[3] > 0 or memo[4] > 0:
            return False
        return True