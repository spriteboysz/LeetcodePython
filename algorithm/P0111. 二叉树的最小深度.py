#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-07 23:14:47
LastEditTime: 2022-03-07 23:22:23
Description: 
FilePath: 111.二叉树的最小深度.py
"""
#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
from math import inf


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        minimum = inf
        if root.left:
            minimum = min(minimum, self.minDepth(root.left))
        if root.right:
            minimum = min(minimum, self.minDepth(root.right))

        return int(minimum + 1)

# @lc code=end
