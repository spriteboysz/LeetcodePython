#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-29 16:15
LastEditTime: 2022-05-29 16:15
Description:
FilePath: 1432.改变一个整数能得到的最大差值.py
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        if len(num) == 1:
            return 8
        min, max = int(num), int(num)
        for i, n in enumerate(num):
            if i == 0 and n != "1":
                min = int(num.replace(n, "1"))
                break
            if n != "0" and n != "1":
                min = int(num.replace(n, "0"))
                break

        for i, n in enumerate(num):
            if n != "9":
                max = int(num.replace(n, "9"))
                break
        print(max, min)
        return max - min


if __name__ == '__main__':
    solution = Solution()
    ans = solution.maxDiff("555")
    print(ans)
    ans = solution.maxDiff("9288")
    print(ans)