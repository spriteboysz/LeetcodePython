#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-23 22:40:07
LastEditTime: 2022-02-23 23:01:18
Description: 
FilePath: 670.最大交换.py
"""


#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(map(int, str(num)))
        last = [None] * 10
        for i in range(len(num)):
            last[num[i]] = i
        for k in range(len(num)):
            for v in range(9, num[k], -1):
                if last[v] is not None and last[v] > k:
                    num[last[v]], num[k] = num[k], num[last[v]]
                    return int("".join(map(str, num)))
        return int("".join(map(str, num)))


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.maximumSwap(2736)
    print(ans)
