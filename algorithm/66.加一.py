#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[i] * 10 ** (len(digits) - i - 1)
        return list(map(int, str(num + 1)))
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    s.plusOne([1, 2, 3])
