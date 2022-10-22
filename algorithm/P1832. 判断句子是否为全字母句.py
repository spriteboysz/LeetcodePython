#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-04 16:36:45
Description:
FilePath: 1832.判断句子是否为全字母句.py
"""


#
# @lc app=leetcode.cn id=1832 lang=python3
#
# [1832] 判断句子是否为全字母句
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for char in range(97, 123):
            if sentence.count(chr(char)) == 0:
                return False
        return True


# @lc code=end

if __name__ == '__main__':
    s = Solution()
    r = s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
    print(r)
