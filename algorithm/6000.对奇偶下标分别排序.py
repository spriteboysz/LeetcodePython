#
# @lc app=leetcode.cn id=6000 lang=python3
#
# [6000] 对奇偶下标分别排序
#

# @lc code=start
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        nums[1::2] = sorted(nums[1::2], reverse=True)
        nums[::2] = sorted(nums[::2])
        return nums
# @lc code=end
