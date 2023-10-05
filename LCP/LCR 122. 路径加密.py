#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-10-02 23:06
FileName: LCP
Description:LCR 122. 路径加密.py 
"""


class Solution:
    def pathEncryption(self, path: str) -> str:
        return path.replace(".", " ")


if __name__ == '__main__':
    print(Solution().pathEncryption(path="a.aef.qerf.bb"))
