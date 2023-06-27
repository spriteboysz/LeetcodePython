#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

from typing import List


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = [i for i in nums1 if i in nums2]
        return list(set(lst))
# @lc code=end
