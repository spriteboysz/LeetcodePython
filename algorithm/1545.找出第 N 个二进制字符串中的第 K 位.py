#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 16:46
LastEditTime: 2022-05-29 16:46
Description:
FilePath: 1545.找出第 N 个二进制字符串中的第 K 位.py
"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n <= 1 and k <= 1:
            return "0"

        def process(num):
            return "".join(
                list(map(lambda el: str(1 - int(el)), list(num)))[::-1])

        sn = "0"
        for i in range(n):
            sn += "1" + process(sn)
        return sn[k - 1]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.findKthBit(n=4, k=11)
    print(ans)
