#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            t3 = t2 + t1 + t0
            t0, t1, t2 = t1, t2, t3
        return t3
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(30))
