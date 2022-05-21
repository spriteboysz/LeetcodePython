#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-20 23:02:15
LastEditTime: 2022-05-20 23:02:16
Description: 
FilePath: 剑指 Offer 32 - III. 从上到下打印二叉树 III.py
"""

from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        values, queue = [], deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(values) % 2 == 0:
                values.append(level)
            else:
                values.append(level[::-1])
        return values
