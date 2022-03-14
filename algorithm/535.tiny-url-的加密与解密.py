#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-14 21:43:23
LastEditTime: 2022-03-14 21:44:51
Description: 
FilePath: 535.tiny-url-的加密与解密.py
"""
#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#

# @lc code=start
from string import ascii_letters, digits
from random import sample


class Codec:
    def __init__(self):
        self.url_dict = {}

    def getKey(self):
        return "".join(sample(ascii_letters + digits, 6))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        tiny = self.getKey()
        while tiny in self.url_dict:
            tiny = self.getKey()
        self.url_dict[tiny] = longUrl
        return "http://tinyurl.com/" + tiny

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.url_dict[shortUrl.replace("http://tinyurl.com/", "")]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
