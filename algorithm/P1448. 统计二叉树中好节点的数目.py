#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-08 00:01:49
LastEditTime: 2022-04-08 00:02:33
Description: 
FilePath: 1448.统计二叉树中好节点的数目.py
"""
#
# @lc app=leetcode.cn id=1448 lang=python3
#
# [1448] 统计二叉树中好节点的数目
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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, current):
            if not root:
                return
            else:
                if root.val >= current:
                    paths.append(root.val)
                    current = root.val
                dfs(root.left, current)
                dfs(root.right, current)

        paths = []
        dfs(root, -inf)
        return len(paths)


# @lc code=end
