#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-29 22:02:17
LastEditTime: 2022-01-29 22:13:00
Description:
FilePath: 1652.拆炸弹.py
"""
#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#

# @lc code=start
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        else:
            code2 = code * 2
            decode = []
            if k > 0:
                for i in range(n):
                    decode.append(sum(code2[i+1:i+k+1]))
            else:
                for i in range(n, n * 2):
                    decode.append(sum(code2[i+k:i]))
            return decode
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.decrypt([5, 7, 1, 4], 3))
    print(s.decrypt([1, 2, 3, 4], 0))
    print(s.decrypt([2, 4, 9, 3], -2))
