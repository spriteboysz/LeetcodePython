from string import ascii_lowercase as lowercase


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m - n) > 1:
            return False
        if m < n:
            return self.oneEditAway(second, first)
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                return (
                    first[i + 1:] == second[i + 1:]
                    if m == n
                    else first[i + 1:] == second[i:]
                )
        return True


if __name__ == "__main__":
    solution = Solution()
    ans = solution.oneEditAway("pale", "ple")
    print(ans)
