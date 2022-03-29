#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-29 23:12:01
LastEditTime: 2022-03-29 23:17:14
Description: 
FilePath: 653.两数之和-iv-输入-bst.py
"""
#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        self.values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.values.append(node.val)
            dfs(node.right)

        dfs(root)
        for i in range(len(self.values) - 1):
            if k - self.values[i] in self.values[i + 1 :]:
                return True
        return False


# @lc code=end
