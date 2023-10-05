#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-03 11:47
FileName: LCP
Description:LCR 130. 衣橱整理.py 
"""


class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        def sums(x):
            ans = 0
            while x:
                ans += x % 10
                x = x // 10
            return ans

        res = {(0, 0)}
        for i in range(m):
            for j in range(n):
                if sums(i) + sums(j) <= cnt and ((i - 1, j) in res or (i, j - 1) in res):
                    res.add((i, j))
        return len(res)


if __name__ == '__main__':
    print(Solution().wardrobeFinishing(m=4, n=7, cnt=5))
