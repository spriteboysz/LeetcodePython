#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-31 00:02:44
LastEditTime: 2022-01-31 00:13:29
Description: 
FilePath: 942.增减字符串匹配.py
'''
#
# @lc app=leetcode.cn id=942 lang=python3
#
# [942] 增减字符串匹配
#

# @lc code=start
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        minimum, maximum = 0, len(s)
        lst = []
        for item in s:
            if item == "I":
                lst.append(minimum)
                minimum += 1
            else:
                lst.append(maximum)
                maximum -= 1
        lst.extend(list({i for i in range(len(s) + 1)} - set(lst)))
        return lst


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.diStringMatch("IDID"))
    print(s.diStringMatch("III"))
    print(s.diStringMatch("DDI"))
