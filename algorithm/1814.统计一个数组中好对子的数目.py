#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-12 22:26
LastEditTime: 2022-06-12 22:26
Description:
FilePath: 1814.统计一个数组中好对子的数目.py
"""

from collections import Counter
from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count, temp = 0, []
        for num in nums:
            temp.append(num - int(str(num)[::-1]))
        # print(temp)

        for v in Counter(temp).values():
            v -= 1
            count += (v + 1) * v // 2
        return count % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.countNicePairs(nums=[42, 11, 1, 79])
    print(ans)
    ans = solution.countNicePairs(nums=[13, 10, 35, 24, 76])
    print(ans)
