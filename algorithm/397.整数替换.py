#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-28 22:40
LastEditTime: 2022-05-28 22:40
Description:
FilePath: 397.整数替换.py
"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        # 如果n等于1，直接返回次数0
        if n == 1:
            return 0
        # 如果n是偶数，则递归计算n/2，递归时次数加1
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        # 如果n是奇数，那么n+1或者n-1一定是偶数，接着计算n/2即可，所以，再递归计算n/2和n/2 + 1的值
        else:
            return 2 + min(self.integerReplacement(n // 2),
                           self.integerReplacement(n // 2 + 1))


if __name__ == '__main__':
    solution = Solution()
    ans = solution.integerReplacement(8)
    print(ans)
