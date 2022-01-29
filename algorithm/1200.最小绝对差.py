#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-29 23:04:37
LastEditTime: 2022-01-29 23:14:44
Description: 
FilePath: 1200.最小绝对差.py
'''
#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        diff = dict()
        for i in range(1, len(arr)):
            cur = arr[i] - arr[i - 1]
            if cur in diff.keys():
                diff[cur].append([arr[i - 1], arr[i]])
            else:
                diff[cur] = [[arr[i - 1], arr[i]]]
        return diff[min(diff.keys())]
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
