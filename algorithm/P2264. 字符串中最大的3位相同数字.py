#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 22:28
LastEditTime: 2022-05-27 22:28
Description:
FilePath: 2264.字符串中最大的3位相同数字.py
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = set()
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                good.add(int(num[i]))
        return str(max(good)) * 3 if good else ""


if __name__ == '__main__':
    solution = Solution()
    ans = solution.largestGoodInteger("2300019")
    print(ans)
