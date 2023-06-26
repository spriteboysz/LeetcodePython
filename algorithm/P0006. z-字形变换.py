#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-16 22:27:50
LastEditTime: 2022-04-16 22:29:34
Description: 
FilePath: 6.z-字形变换.py
"""


#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        ret = [""] * numRows
        i, flag = 0, -1
        for item in s:
            ret[i] += item
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(ret)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.convert(s="PAYPALISHIRING", numRows=4)
    print(ans)
