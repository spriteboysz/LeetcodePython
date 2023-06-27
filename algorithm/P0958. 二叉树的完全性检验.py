#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-13 23:09
LastEditTime: 2022-06-13 23:09
Description:
FilePath: 958.二叉树的完全性检验.py
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue, flag = deque([root]), False
        while queue:
            node = queue.popleft()
            if not node:
                flag = True
                continue
            if flag:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True
