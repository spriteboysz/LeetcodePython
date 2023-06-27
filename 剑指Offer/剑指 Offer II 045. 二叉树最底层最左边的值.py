#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 22:30:02
LastEditTime: 2022-05-21 22:30:03
Description: 
FilePath: 剑指 Offer II 045. 二叉树最底层最左边的值.py
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return

        values, queue = [], deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            values.append(level[0])
        return values[-1]
