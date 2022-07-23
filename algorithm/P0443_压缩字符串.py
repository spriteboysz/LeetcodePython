#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-26 17:14:05
LastEditTime: 2022-03-11 23:07:24
Description: 
FilePath: 443.压缩字符串.py
"""
#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        counts = [1] * len(chars)
        for i in range(1, len(chars)):
            if chars[i - 1] == chars[i]:
                counts[i] = counts[i - 1] + 1
                counts[i - 1] = 0
        tmp = []
        for char, count in filter(lambda el: el[1] != 0, zip(chars, counts)):
            tmp.append(char)
            if count >= 2:
                tmp.extend(list(str(count)))
        chars[:] = tmp
        return len(chars)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.compress(["a", "a", "b", "b", "c", "c", "c"])
    print(ans)
    ans = solution.compress(["a"])
    print(ans)
    ans = solution.compress(
        ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    )
    print(ans)
