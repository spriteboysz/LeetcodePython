#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-05-21 22:25:55
LastEditTime: 2022-05-21 22:25:55
Description: 
FilePath: 剑指 Offer II 044. 二叉树每层的最大值.py
"""

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
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
            values.append(max(level))
        return values
