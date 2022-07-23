#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-14 23:02:01
LastEditTime: 2022-01-14 23:13:59
Description: 
FilePath: 205.同构字符串.py
'''
#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            mapping = dict()
            for k, v in zip(list(s), list(t)):
                if k not in mapping.keys():
                    mapping[k] = v
                else:
                    if mapping[k] != v:
                        return False
            mapping = dict()
            for k, v in zip(list(t), list(s)):
                if k not in mapping.keys():
                    mapping[k] = v
                else:
                    if mapping[k] != v:
                        return False
            else:
                return True

# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic("badc", "baba"))
