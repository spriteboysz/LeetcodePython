#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = abs(n)
        power = 1
        for i in range(1, n + 1):
            power *= x
            if abs(power) < 0.0001:
                return 0.00000

        return power
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.0, 0))
