#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 16:31
LastEditTime: 2022-05-29 16:31
Description:
FilePath: 1405.最长快乐字符串.py
"""


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        numcount = {"a": a, "b": b, "c": c}
        diverse = ""
        while True:
            less, mid, most = sorted(
                numcount.keys(), key=lambda el: numcount[el])
            if (len(diverse) < 2 or not diverse[-2] ==
                    diverse[-1] == most) and numcount[most] > 0:
                diverse += most
                numcount[most] -= 1
            elif (not diverse[-2] == diverse[-1] == mid) and numcount[mid] > 0:
                diverse += mid
                numcount[mid] -= 1
            else:
                return diverse


if __name__ == '__main__':
    solution = Solution()
    ans = solution.longestDiverseString(a=1, b=1, c=7)
    print(ans)
