#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-30 23:32
LastEditTime: 2022-05-30 23:32
Description:
FilePath: 1015.可被 K 整除的最小整数.py
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if str(k)[-1] not in ["1", "3", "7", "9"]:
            return -1

        cur = 1
        while True:
            if cur % k != 0:
                cur = cur * 10 + 1
            else:
                return len(str(cur))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.smallestRepunitDivByK(3)
    print(ans)
