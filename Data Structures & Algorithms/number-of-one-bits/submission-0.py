class Solution:
    def hammingWeight(self, n: int) -> int:
        a = bin(n)[2:]
        binary_str = f"{n:b}"
        l = list(binary_str)
        b = 0
        for i in range(len(l)):
            if l[i] == '1':
                b += 1
        return b