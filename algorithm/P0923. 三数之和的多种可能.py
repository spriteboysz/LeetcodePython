#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-15 22:04:06
LastEditTime: 2022-03-15 22:20:25
Description: 
FilePath: 923.三数之和的多种可能.py
"""
#
# @lc app=leetcode.cn id=923 lang=python3
#
# [923] 三数之和的多种可能
#

from collections import defaultdict
# @lc code=start
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        numcount = defaultdict(int)
        for num in arr:
            numcount[num] += 1
        count = 0
        for i in range(target + 1):
            if i not in numcount:
                continue
            for j in range(i, target + 1):
                if j not in numcount:
                    continue
                k = target - i - j
                if k >= j and k in numcount:
                    if i == j == k:
                        count += (
                                numcount[i] * (numcount[i] - 1) * (numcount[i] - 2) // 6
                        )
                    elif i == j != k:
                        count += numcount[i] * (numcount[i] - 1) // 2 * numcount[k]
                    elif i != j == k:
                        count += numcount[i] * numcount[j] * (numcount[j] - 1) // 2
                    else:
                        count += numcount[i] * numcount[j] * numcount[k]
        return count % (10 ** 9 + 7)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8)
    print(ans)
