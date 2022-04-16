#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-11 22:08:21
LastEditTime: 2022-04-16 22:42:22
Description: 
FilePath: 17.电话号码的字母组合.py
"""
#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        keyboard = [0, 1, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        queue = list(keyboard[int(digits[0])])
        for num in digits[1:]:
            curlevel = []
            while queue:
                prefix = queue.pop(0)
                for letter in keyboard[int(num)]:
                    curlevel.append(prefix + letter)
            queue = curlevel
        return queue


# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("24"))
    print(s.letterCombinations("234"))
