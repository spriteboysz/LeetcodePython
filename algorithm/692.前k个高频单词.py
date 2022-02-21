#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-21 23:42:43
LastEditTime: 2022-02-21 23:47:30
Description: 
FilePath: 692.前k个高频单词.py
"""
#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1
        counts = sorted(list(counts.items()), key=lambda el: (-el[1], el[0]))
        return [word[0] for i, word in enumerate(counts) if i < k]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
    print(ans)
    ans2 = solution.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    )
    print(ans2)
