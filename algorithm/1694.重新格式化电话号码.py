#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-30 22:40:50
LastEditTime: 2022-01-30 22:49:35
Description: 
FilePath: 1694.重新格式化电话号码.py
'''
#
# @lc app=leetcode.cn id=1694 lang=python3
#
# [1694] 重新格式化电话号码
#

# @lc code=start


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(" ", "").replace("-", "")
        reformat = ""
        if len(number) % 3 == 0:
            for i, item in enumerate(number):
                if i and i % 3 == 0:
                    reformat += "-"
                reformat += item
        elif len(number) % 3 == 1:
            for i, item in enumerate(number[:-4]):
                if i and i % 3 == 0:
                    reformat += "-"
                reformat += item
            reformat += "-" + number[-4:-2] + "-" + number[-2:]
        else:
            for i, item in enumerate(number[:-2]):
                if i and i % 3 == 0:
                    reformat += "-"
                reformat += item
            reformat += "-" + number[-2:]
        return reformat.lstrip("-")
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.reformatNumber("12"))
    print(s.reformatNumber("123 4-5678"))
