#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-04 21:48:00
LastEditTime: 2022-04-04 21:55:22
Description: 
FilePath: 2191.将杂乱无章的数字排序.py
"""
#
# @lc app=leetcode.cn id=2191 lang=python3
#
# [2191] 将杂乱无章的数字排序
#

# @lc code=start
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = (
                num,
                int("".join(map(lambda el: str(mapping[int(el)]), str(num)))),
            )

        return list(map(lambda el: el[0], sorted(nums, key=lambda el: el[1])))


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.sortJumbled(
        mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]
    )
    print(ans)

    ans = solution.sortJumbled(
        mapping=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], nums=[789, 456, 123]
    )
    print(ans)
