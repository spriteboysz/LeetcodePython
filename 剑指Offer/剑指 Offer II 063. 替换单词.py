#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-17 23:11:05
LastEditTime: 2022-05-17 23:11:05
Description: 
FilePath: 剑指 Offer II 063. 替换单词.py
"""

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        words = []
        for word in sentence.split():
            for root in dictionary:
                if word.startswith(root):
                    words.append(root)
                    break
            else:
                words.append(word)
        return " ".join(words)


if __name__ == "__main__":
    solution = Solution()
    ans = solution.replaceWords(
        dictionary=["cat", "bat", "rat"],
        sentence="the cattle was rattled by the battery",
    )
    print(ans)
    ans = solution.replaceWords(
        dictionary=["a", "b", "c"], sentence="aadsfasf absbs bbab cadsfafs"
    )
    print(ans)
    ans = solution.replaceWords(
        dictionary=["a", "aa", "aaa", "aaaa"],
        sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa",
    )
    print(ans)
    ans = solution.replaceWords(
        dictionary=["catt", "cat", "bat", "rat"],
        sentence="the cattle was rattled by the battery",
    )
    print(ans)
    ans = solution.replaceWords(
        dictionary=["ac", "ab"],
        sentence="it is abnormal that this solution is accepted",
    )
    print(ans)
