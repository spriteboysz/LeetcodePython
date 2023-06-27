#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-07 22:18:48
LastEditTime: 2022-02-07 22:28:37
Description:
FilePath: 1128.等价多米诺骨牌对的数量.py
"""
#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        points = [0] * 100
        for domino in dominoes:
            points[min(domino) * 10 + max(domino)] += 1
        count = 0
        for point in filter(lambda el: el >= 2, points):
            count += sum(range(1, point))
        return count


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
    print(s.numEquivDominoPairs(
        [[2, 1], [5, 4], [3, 7], [6, 2], [4, 4], [1, 8], [9, 6], [5, 3], [7, 4], [1, 9], [1, 1], [6, 6], [9, 6], [
            1, 3], [9, 7], [4, 7], [5, 1], [6, 5], [1, 6], [6, 1], [1, 8], [7, 2], [2, 4], [1, 6], [3, 1], [3, 9],
         [3, 7], [9, 1], [1, 9], [8, 9]]))
