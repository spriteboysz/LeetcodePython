#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 22:18
LastEditTime: 2022-05-27 22:18
Description:
FilePath: 2269.找到一个数字的K美丽值.py
"""


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s, count = str(num), 0
        for i in range(len(s) - k + 1):
            cur = int(s[i: i + k])
            if cur != 0 and num % cur == 0:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    ans = solution.divisorSubstrings(430043, 2)
    print(ans)
