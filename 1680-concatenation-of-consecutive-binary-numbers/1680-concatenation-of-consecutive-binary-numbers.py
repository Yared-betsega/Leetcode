class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int("".join(list(map(lambda x: bin(x)[2:], range(1, n + 1)))), 2) % (10 ** 9 + 7)