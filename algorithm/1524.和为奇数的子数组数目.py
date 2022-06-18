#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-18 21:51
LastEditTime: 2022-06-18 21:51
Description:
FilePath: 1524.和为奇数的子数组数目.py
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        sums, odd, even = [0], 0, 0
        for i, num in enumerate(arr):
            sums.append(sums[-1] + num)
            if sums[-1] % 2 == 0:
                even += 1
            else:
                odd += 1
        return (odd + odd * even) % (10 ** 9 + 7)


if __name__ == '__main__':
    solution = Solution()
    ans = solution.numOfSubarrays(arr=[1, 3, 5])
    print(ans)
    ans = solution.numOfSubarrays(arr=[1, 2, 3, 4, 5, 6, 7])
    print(ans)
