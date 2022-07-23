#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-15 00:01:27
LastEditTime: 2022-01-15 00:09:41
Description: 
FilePath: 290.单词规律.py
'''
#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(list(pattern)) != len(s.split()):
            return False
        else:
            mapping = dict()
            for i, v in zip(list(pattern), s.split()):
                if i not in mapping.keys():
                    mapping[i] = v
                else:
                    if mapping[i] != v:
                        return False
            mapping = dict()
            for i, v in zip(s.split(), list(pattern)):
                if i not in mapping.keys():
                    mapping[i] = v
                else:
                    if mapping[i] != v:
                        return False
            else:
                return True
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern("abba", "dog cat cat dog"))
    print(s.wordPattern("aaa", "aa aa aa aa"))
