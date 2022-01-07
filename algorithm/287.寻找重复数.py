#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            lst[nums[i]] += 1

        for j in range(1, len(nums) + 2):
            if lst[j] > 1:
                return j
# @lc code=end
