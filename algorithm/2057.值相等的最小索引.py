#
# @lc app=leetcode.cn id=2057 lang=python3
#
# [2057] 值相等的最小索引
#

# @lc code=start
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if index % 10 == num:
                return index
        return -1
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.smallestEqual([0, 1, 2]))
    print(s.smallestEqual([4, 3, 2, 1]))
    print(s.smallestEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(s.smallestEqual([2, 1, 3, 5, 2]))
