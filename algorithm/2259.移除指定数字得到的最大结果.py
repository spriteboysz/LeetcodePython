#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 22:38
LastEditTime: 2022-05-27 22:38
Description:
FilePath: 2259.移除指定数字得到的最大结果.py
"""


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n, index = len(number), len(number)
        for i in range(n):
            if number[i] == digit:
                index = i
                if i + 1 < n and number[i + 1] > digit:
                    break
        return number[:index] + number[index + 1:]


if __name__ == '__main__':
    solution = Solution()
    ans = solution.removeDigit("1231", "1")
    print(ans)
