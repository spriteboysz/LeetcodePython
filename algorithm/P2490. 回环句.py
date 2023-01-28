#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023/1/28 23:37
FileName: algorithm/P2490. 回环句.py
Description: 
"""


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        flag = True
        for i in range(len(words)):
            if i == 0:
                if words[-1][-1] != words[0][0]:
                    flag = False
                    break
            else:
                if words[i - 1][-1] != words[i][0]:
                    flag = False
                    break
        return flag


if __name__ == '__main__':
    print(Solution().isCircularSentence(sentence="leetcode exercises sound delightful"))
    print(Solution().isCircularSentence(sentence="leetcode"))
