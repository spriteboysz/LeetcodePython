#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-24 23:01
LastEditTime: 2022-05-24 23:01
Description:
FilePath: 面试题 17.16. 按摩师.py
"""

from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
        return now


if __name__ == '__main__':
    solution = Solution()
    ans = solution.massage([2, 4, 9, 3, 1])
    print(ans)
