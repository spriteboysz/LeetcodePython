#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-12 17:59
LastEditTime: 2022-06-12 17:59
Description:
FilePath: 1813.句子相似性 III.py
"""


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1, words2 = sentence1.split(), sentence2.split()
        n1, n2 = len(words1), len(words2)
        if n1 == n2:
            return sentence1 == sentence2
        if n1 < n2:
            n1, n2, words1, words2 = n2, n1, words2, words1

        while words2:
            if words1[0] != words2[0] and words1[-1] != words2[-1]:
                return False
            if words1[0] == words2[0]:
                words1.pop(0)
                words2.pop(0)
            if words2 and words1[-1] == words2[-1]:
                words1.pop()
                words2.pop()
        return True


if __name__ == '__main__':
    solution = Solution()
    ans = solution.areSentencesSimilar(
        sentence1="My name is Haley",
        sentence2="My Haley")
    print(ans)
    ans = solution.areSentencesSimilar(
        sentence1="of", sentence2="A lot of words")
    print(ans)
    ans = solution.areSentencesSimilar(
        sentence1="Eating right now",
        sentence2="Eating")
    print(ans)
    ans = solution.areSentencesSimilar(sentence1="Luky", sentence2="Lucccky")
    print(ans)
