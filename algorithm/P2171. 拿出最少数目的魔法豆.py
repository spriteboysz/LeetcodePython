#
# @lc app=leetcode.cn id=2171 lang=python3
#
# [2171] 拿出最少数目的魔法豆
#

# @lc code=start
from typing import List


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        count = 0
        for i, v in enumerate(sorted(beans, reverse=True)):
            count = max(count, (i + 1) * v)
        return sum(beans) - count


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.minimumRemoval([4, 1, 6, 5])
    print(ans)
