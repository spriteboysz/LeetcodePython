#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(list(set(nums)))
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 4, 1]))
