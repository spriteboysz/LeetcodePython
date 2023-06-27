#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 14:57
LastEditTime: 2022-06-19 14:57
Description:
FilePath: 剑指 Offer 51. 数组中的逆序对.py
"""

from typing import List

from sortedcontainers import SortedList


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sl, count = SortedList(), 0
        for i in range(len(nums) - 1, -1, -1):  # 反向遍历
            count += sl.bisect_left(nums[i])  # 找到右边比当前值小的元素个数
            sl.add(nums[i])  # 将当前值加入有序数组中

        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.reversePairs([7, 5, 6, 4])
    print(ans)
