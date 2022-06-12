#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-12 16:44
LastEditTime: 2022-06-12 16:44
Description:
FilePath: 1797.设计一个验证系统.py
"""

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.tokens.get(tokenId, -self.ttl) + self.ttl > currentTime:
            self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return len(list(filter(lambda time: time + self.ttl > currentTime, self.tokens.values())))

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
