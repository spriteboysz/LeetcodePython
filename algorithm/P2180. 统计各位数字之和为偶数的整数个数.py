#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-01 23:34:38
LastEditTime: 2022-03-01 23:37:19
Description:
FilePath: 6012.统计各位数字之和为偶数的整数个数.py
"""


#
# @lc app=leetcode.cn id=6012 lang=python3
#
# [6012] 统计各位数字之和为偶数的整数个数
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2, num + 1):
            if sum(map(int, str(i))) % 2 == 0:
                count += 1
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.countEven(4)
    print(ans)
    ans = solution.countEven(100)
    print(ans)
