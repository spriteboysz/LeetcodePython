#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-02-05 23:40:11
LastEditTime: 2022-02-05 23:45:30
Description: 
FilePath: 49.字母异位词分组.py
'''
#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = dict()
        for word in strs:
            cur = "".join(sorted(word))
            if cur in alphabet.keys():
                alphabet[cur].append(word)
            else:
                alphabet[cur] = [word]
        return [el for el in alphabet.values()]

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.groupAnagrams([""]))
    print(s.groupAnagrams(["a"]))
