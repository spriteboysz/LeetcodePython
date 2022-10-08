#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-22 22:23:03
LastEditTime: 2022-04-22 22:27:51
Description: 
FilePath: 954.二倍数对数组.py
"""
#
# @lc app=leetcode.cn id=954 lang=python3
#
# [954] 二倍数对数组
#

from collections import defaultdict
# @lc code=start
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        print(count)

        for num in sorted(count, key=abs):
            # print(num, count[num])
            if count[num] > count[2 * num]:
                return False
            count[2 * num] -= count[num]
        return True


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.canReorderDoubled([4, -2, 2, -4])
    print(ans)
