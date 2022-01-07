#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-04 16:17:40
Description: 将句子排序
FilePath: 1859.将句子排序.py
'''
#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#

# @lc code=start


class Solution:
    def sortSentence(self, s: str) -> str:
        lst2 = []
        for item in s.split():
            lst2.append(item[::-1])

        lst3 = []
        for item in sorted(lst2):
            lst3.append(item[:0:-1])
        return " ".join(lst3)
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.sortSentence("is2 sentence4 This1 a3"))
