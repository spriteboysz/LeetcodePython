#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num != 0 and num % 9 == 0:
            return 9
        else:
            return num % 9
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(90))
