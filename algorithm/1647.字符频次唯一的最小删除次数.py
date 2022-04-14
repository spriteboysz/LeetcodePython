#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-14 23:49:07
LastEditTime: 2022-04-14 23:53:32
Description: 
FilePath: 1647.字符频次唯一的最小删除次数.py
"""
#
# @lc app=leetcode.cn id=1647 lang=python3
#
# [1647] 字符频次唯一的最小删除次数
#

# @lc code=start
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count, seen = 0, set()
        for v in Counter(s).values():
            cur = v
            while cur > 0 and cur in seen:
                cur -= 1
            count += v - cur
            if cur > 0:
                seen.add(cur)
        return count


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    ans = solution.minDeletions("aaabbbcc")
    print(ans)
