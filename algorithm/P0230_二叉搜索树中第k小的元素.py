#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-27 23:16:19
LastEditTime: 2022-03-27 23:21:32
Description: 
FilePath: 230.二叉搜索树中第k小的元素.py
"""
#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.values.append(node.val)
            dfs(node.right)

        self.values = []
        dfs(root)
        return self.values[k - 1]


# @lc code=end
