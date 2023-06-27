#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 16:26:23
LastEditTime: 2022-04-05 16:29:59
Description: 
FilePath: 897.递增顺序搜索树.py
"""


#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        if not root or (not root.left and not root.right):
            return root

        dfs(root)
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]

# @lc code=end
