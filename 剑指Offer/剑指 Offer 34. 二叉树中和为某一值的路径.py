#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-06-04 17:03
LastEditTime: 2022-06-04 17:03
Description:
FilePath: 剑指 Offer 34. 二叉树中和为某一值的路径.py
"""

from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        paths, path = [], []

        def recur(node, target):
            if not node:
                return
            path.append(node.val)
            target -= node.val
            if target == 0 and not node.left and not node.right:
                paths.append(list(path))
            recur(node.left, target)
            recur(node.right, target)
            path.pop()

        recur(root, target)
        return paths
