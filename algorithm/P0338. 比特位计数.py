#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(0, n + 1):
            s = bin(i).count("1")
            lst.append(s)
        return lst
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(5))
