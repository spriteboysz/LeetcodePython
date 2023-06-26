#!/usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-01-21 23:32:54
LastEditTime: 2022-01-21 23:45:10
Description:
FilePath: 2062.统计字符串中的元音子字符串.py
"""
#
# @lc app=leetcode.cn id=2062 lang=python3
#
# [2062] 统计字符串中的元音子字符串
#

# @lc code=start


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        for i in range(len(word) - 4):
            for j in range(i + 4, len(word)):
                if list(sorted(set(list(word[i:j + 1])))) == ["a", "e", "i", "o", "u"]:
                    count += 1
        return count
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    print(s.countVowelSubstrings("unicornarihan"))
    print(s.countVowelSubstrings("cuaieuouac"))
    print(s.countVowelSubstrings("bbaeixoubb"))
