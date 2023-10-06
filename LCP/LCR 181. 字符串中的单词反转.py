#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-04 00:02
FileName: LCP
Description:LCR 181. 字符串中的单词反转.py 
"""


class Solution:
    def reverseMessage(self, message: str) -> str:
        return " ".join(message.strip().split()[::-1])


if __name__ == '__main__':
    print(Solution().reverseMessage(message="the sky is blue"))
