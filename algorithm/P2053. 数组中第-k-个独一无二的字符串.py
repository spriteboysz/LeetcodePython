#
# @lc app=leetcode.cn id=2053 lang=python3
#
# [2053] 数组中第 K 个独一无二的字符串
#

# @lc code=start
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = list(filter(lambda el: arr.count(el) == 1, arr))
        if len(distinct) < k:
            return ""
        else:
            return distinct[k - 1]
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.kthDistinct(["d", "b", "c", "b", "c", "a"], 2))
    print(s.kthDistinct(["aaa", "aa", "a"], 1))
    print(s.kthDistinct(["a", "b", "a"], 3))
