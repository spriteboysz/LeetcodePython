#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]

        return len(nums)

