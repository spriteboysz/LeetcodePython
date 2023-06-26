#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-10 22:46:30
LastEditTime: 2022-02-10 22:59:34
Description:
FilePath: 451.根据字符出现频率排序.py
"""
#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start


class Solution:
    def frequencySort(self, s: str) -> str:
        count = dict()
        for item in s:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        count = sorted(count.items(), key=lambda el: el[1], reverse=True)
        return "".join([el[0] * el[1] for el in count])
# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("tree"))
    print(s.frequencySort("cccaaa"))
    print(s.frequencySort("Aabb"))
