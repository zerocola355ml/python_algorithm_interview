# Answer1
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum = 0

        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            sum = A ^ B ^ carry
            carry = ((A | B) & carry) | (A & B)
            result.append(str(sum))

        ''' 사실 없어도 됨
        if carry == 1:
            result.append('1') 
        '''
        result = int(''.join(result[::-1]), 2) & MASK

        if result > INT_MAX:  # result // (2**31) == 1 도 가능
            result = ~(result ^ MASK)
        return result