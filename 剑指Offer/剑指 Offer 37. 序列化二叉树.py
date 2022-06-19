#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 14:25
LastEditTime: 2022-06-19 14:25
Description:
FilePath: 剑指 Offer 37. 序列化二叉树.py
"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        if not root:
            return "[]"
        serial, queue = [], deque([root])
        while queue:
            node = queue.popleft()
            if node:
                serial.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serial.append("#")
        return "[" + ",".join(serial) + "]"


    def deserialize(self, data):
        if data == "[]":
            return
        values, index = data[1:-1].split(","), 1
        root = TreeNode(int(values[0]))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if values[index] != "#":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1
            if values[index] != "#":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1
        return root
