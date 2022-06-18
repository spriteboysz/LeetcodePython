#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-17 23:25
LastEditTime: 2022-06-17 23:25
Description:
FilePath: 1472.设计浏览器历史记录.py
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.position = 0

    def visit(self, url: str) -> None:
        while len(self.stack) != self.positon + 1:
            self.stack.pop()
        self.stack.append(url)
        self.position += 1

    def back(self, steps: int) -> str:
        self.position = max(self.position - steps, 0)
        return self.stack[self.position]

    def forward(self, steps: int) -> str:
        self.position = min(self.position + steps, len(self.stack) - 1)
        return self.stack[self.position]


