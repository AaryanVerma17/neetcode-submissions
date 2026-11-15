class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        string = str(abs(x))
        reversed_string = string[::-1]
        reversed_int = sign * int(reversed_string)
        if -2**31 <= reversed_int <= 2**31 - 1:
            return reversed_int
        else:
            return 0