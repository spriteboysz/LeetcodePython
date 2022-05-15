class Solution:
    def waysToStep(self, n: int) -> int:
        a, b, c = 4, 2, 1
        if n < 3:
            return n
        if n == 3:
            return 4
        for _ in range(n - 3):
            a, b, c = (a + b + c) % 1000000007, a, b
        return a

if __name__ == "__main__":
    solution = Solution()
    ans = solution.waysToStep(5)
    print(ans)
