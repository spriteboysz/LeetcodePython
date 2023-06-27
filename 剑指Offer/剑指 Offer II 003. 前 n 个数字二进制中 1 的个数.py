#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-15 16:53:52
LastEditTime: 2022-05-15 16:57:16
Description:
FilePath: 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数.py
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count("1") for i in range(n + 1)]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.countBits(5)
    print(ans)
