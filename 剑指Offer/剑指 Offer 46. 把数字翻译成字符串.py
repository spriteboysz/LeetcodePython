#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-05 14:02
LastEditTime: 2022-06-05 14:02
Description:
FilePath: 剑指 Offer 46. 把数字翻译成字符串.py
"""


class Solution:
    def translateNum(self, num: int) -> int:
        s, a, b = str(num), 1, 1
        for i in range(2, len(s) + 1):
            a, b = a + b if "10" <= s[i - 2:i] <= "25" else a, a
        return a


if __name__ == '__main__':
    solution = Solution()
    ans = solution.translateNum(12258)
    print(ans)
