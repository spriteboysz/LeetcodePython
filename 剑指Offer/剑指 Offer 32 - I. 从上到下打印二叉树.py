#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-20 22:52:04
LastEditTime: 2022-05-20 22:52:05
Description: 
FilePath: 剑指 Offer 32 - I. 从上到下打印二叉树.py
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
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        values, queue = [], deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return values
