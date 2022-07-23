#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-28 22:48:27
Description: 
FilePath: 824.山羊拉丁文.py
'''
#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lst1 = sentence.strip().split()
        lst2 = []
        vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        for i, word in enumerate(lst1):
            if word.startswith(vowel):
                word += "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word += "a" * (i + 1)
            lst2.append(word)

        return " ".join(lst2)
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    latin = s.toGoatLatin("I Opeak Goat Latin")
    print(latin)
