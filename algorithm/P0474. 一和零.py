#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-03 16:09
FileName: LCP
Description:P0474. 一和零.py 
"""
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 默认初始化0
        for ss in strs:
            ones = ss.count('1')
            zeros = ss.count('0')
            # 遍历背包容量且从后向前遍历！
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]


if __name__ == '__main__':
    print(Solution().findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
