#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 14:54:24
LastEditTime: 2022-03-19 14:56:53
Description: 
FilePath: 513.找树左下角的值.py
"""
#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxlevel, self.target = 0, root.val

        def dfs(node, level):
            if not node:
                return
            if not node.left and not node.right:
                if level > self.maxlevel:
                    self.maxlevel = level
                    self.target = node.val
            else:
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 0)
        return self.target


# @lc code=end
