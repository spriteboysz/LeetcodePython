#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 22:12
FileName: LCP
Description:LCR 063. 单词替换.py 
"""
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        dic = {}
        words = sentence.strip().split()
        for i, word in enumerate(words):
            if word in dic:
                words[i] = dic[word]
            else:
                for root in dictionary:
                    if word.startswith(root):
                        words[i] = root
                        dic[word] = root
                        break
        return " ".join(words)


if __name__ == '__main__':
    print(Solution().replaceWords(dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery"))
    print(Solution().replaceWords(dictionary=["aa", "a", "aaa", "aaaa"],
                                  sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
