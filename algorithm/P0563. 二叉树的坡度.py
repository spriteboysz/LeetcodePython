#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 21:09:53
LastEditTime: 2022-04-05 21:13:07
Description: 
FilePath: 563.二叉树的坡度.py
"""
#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            leftdiff, leftsum = dfs(node.left)
            rightdiff, rightsum = dfs(node.right)
            return (
                leftdiff + rightdiff + abs(leftsum - rightsum),
                leftsum + rightsum + node.val,
            )

        return dfs(root)[0]


# @lc code=end
