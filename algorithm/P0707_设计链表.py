#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-10 23:00:03
LastEditTime: 2022-04-10 23:07:44
Description: 
FilePath: 707.设计链表.py
"""
#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class MyLinkedList:
    def __init__(self):
        self.nodes = []

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.nodes):
            return -1
        else:
            return self.nodes[index]

    def addAtHead(self, val: int) -> None:
        self.nodes.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.nodes.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.nodes.insert(0, val)
        elif 0 <= index <= len(self.nodes):
            self.nodes.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.nodes):
            del self.nodes[index]


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
