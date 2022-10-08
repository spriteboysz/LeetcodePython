#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 09:48
LastEditTime: 2022-06-04 09:48
Description:
FilePath: 2283.判断一个数的数字计数是否等于数位的值.py
"""


class Solution:
    def digitCount(self, num: str) -> bool:
        for i, n in enumerate(num):
            if num.count(str(i)) != int(n):
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    ans = solution.digitCount(num="1210")
    print(ans)
