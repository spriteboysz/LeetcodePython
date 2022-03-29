#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-29 23:01:15
LastEditTime: 2022-03-29 23:04:53
Description: 
FilePath: 257.二叉树的所有路径.py
"""
#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return
        paths, queue = [], deque()
        queue.append((root, str(root.val)))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                paths.append(path)
            path += "->"
            if node.left:
                queue.append((node.left, path + str(node.left.val)))
            if node.right:
                queue.append((node.right, path + str(node.right.val)))
        return paths


# @lc code=end
