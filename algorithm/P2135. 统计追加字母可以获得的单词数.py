#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-20 15:03:56
LastEditTime: 2022-03-20 15:07:40
Description: 
FilePath: 2135.统计追加字母可以获得的单词数.py
"""
#
# @lc app=leetcode.cn id=2135 lang=python3
#
# [2135] 统计追加字母可以获得的单词数
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startcounts = Counter(["".join(sorted(i)) for i in startWords])

        count = 0
        for target in targetWords:
            for j in range(len(target)):
                cursorted = "".join(sorted(target[:j] + target[j + 1:]))
                if cursorted in startcounts:
                    count += 1
                    break
        return count


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.wordCount(
        startWords=["ant", "act", "tack"], targetWords=["tack", "act", "acti"]
    )
    print(ans)

    ans = solution.wordCount(
        ["g", "vf", "ylpuk", "nyf", "gdj", "j", "fyqzg", "sizec"],
        ["r", "am", "jg", "umhjo", "fov", "lujy", "b", "uz", "y"],
    )
    print(ans)
