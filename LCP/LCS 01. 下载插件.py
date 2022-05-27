#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-27 23:05
LastEditTime: 2022-05-27 23:05
Description: 
FilePath: LCS 01. 下载插件.py
"""


class Solution:
    def leastMinutes(self, n: int) -> int:
        minimum, speed = 1, 1
        while n > 0:
            if n > speed:
                minimum += 1
                speed *= 2
            else:
                return minimum
    
    
if __name__ == '__main__':
    solution = Solution()
    ans = solution.leastMinutes(4)
    print(ans)
    