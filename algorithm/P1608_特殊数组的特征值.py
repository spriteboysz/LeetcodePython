#
# @lc app=leetcode.cn id=1608 lang=python3
#
# [1608] 特殊数组的特征值
#

# @lc code=start
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(max(nums), -1, -1):
            if len(list(filter(lambda el: el >= i, nums))) == i:
                return i
        return -1
# @lc code=end
