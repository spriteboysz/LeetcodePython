#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-01 00:17:53
LastEditTime: 2022-05-01 00:19:43
Description: 
FilePath: 剑指 Offer 58 - II. 左旋转字符串.py
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


if __name__ == "__main__":
    solution = Solution()
    ans = solution.reverseLeftWords(s="lrloseumgh", n=6)
    print(ans)
