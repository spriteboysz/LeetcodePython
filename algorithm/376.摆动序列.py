#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-03 21:58
LastEditTime: 2022-06-03 21:58
Description:
FilePath: 376.摆动序列.py
"""

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        c, count, n = 0, 1, len(nums)
        if n < 2:
            return n
        for i in range(1, n):
            x = nums[i] - nums[i - 1]
            if x:
                if x * c <= 0:
                    count += 1
                c = x
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.wiggleMaxLength([1, 7, 4, 9, 2, 5])
    print(ans)
