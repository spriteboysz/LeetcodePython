class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        for k in range(i, j + 1):
            N &= ~(1 << k)
        return N | (M << i)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.insertBits(1024, 19, 2, 6)
    print(ans)
