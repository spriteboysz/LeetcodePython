#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-18 22:38:54
LastEditTime: 2022-03-18 22:53:19
Description: 
FilePath: 393.utf-8-编码验证.py
"""
#
# @lc app=leetcode.cn id=393 lang=python3
#
# [393] UTF-8 编码验证
#

# @lc code=start
from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        bytes = 0
        for item in data:
            if bytes > 0:
                if 128 <= item < 192:
                    bytes -= 1
                else:
                    return False
            elif bytes == 0:
                if item < 128:
                    bytes = 0
                elif 192 <= item < 224:
                    bytes = 1
                elif 224 <= item < 240:
                    bytes = 2
                elif 240 <= item < 248:
                    bytes = 3
                else:
                    return False
        return bytes == 0


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.validUtf8([197, 130, 1])
    print(ans)
    ans = solution.validUtf8([235, 140, 4])
    print(ans)
    ans = solution.validUtf8([237])
    print(ans)
