#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-29 00:00:45
LastEditTime: 2022-01-29 00:06:32
Description:
FilePath: 482.密钥格式化.py
"""


#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace("-", "")
        start = len(s) % k
        key = s[:start]
        for i, item in enumerate(s[start:]):
            if i % k == 0:
                key += "-"
            key += item
        return key.lstrip("-")


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.licenseKeyFormatting("5F3Z-2e-9-w", 4))
