#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-19 22:48
LastEditTime: 2022-06-19 22:48
Description:
FilePath: 剑指 Offer II 048. 序列化与反序列化二叉树.py
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
            return ""
        serial, queue = [], deque([root])
        while queue:
            node = queue.popleft()
            if node:
                serial.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serial.append("#")
        return ",".join(serial)

    def deserialize(self, data):
        if not data:
            return []
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue, i = deque([root]), 1
        while queue:
            node = queue.popleft()
            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
        return root
