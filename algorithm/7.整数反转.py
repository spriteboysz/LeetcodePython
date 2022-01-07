#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        return int(str(x)[::-1])
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    