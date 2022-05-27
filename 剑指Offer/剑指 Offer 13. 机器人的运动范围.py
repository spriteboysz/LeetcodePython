#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-26 23:11
LastEditTime: 2022-05-26 23:11
Description:
FilePath: 剑指 Offer 13. 机器人的运动范围.py
"""

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def stat(num):
            return sum(map(int, list(str(num))))

        res = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if stat(i) + stat(j) <= k and (((i - 1), j)
                                               in res or (i, j - 1) in res):
                    res.add((i, j))
        return len(res)

if __name__ == '__main__':
    solution = Solution()
    ans = solution.movingCount(m=2, n=3, k=1)
    print(ans)
