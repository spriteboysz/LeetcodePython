#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-30 23:24:18
LastEditTime: 2022-03-30 23:29:12
Description: 
FilePath: 114.二叉树展开为链表.py
"""
#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if not node:
                return
            self.nodes.append(node)
            dfs(node.left)
            dfs(node.right)

        self.nodes = []
        dfs(root)

        for i in range(len(self.nodes) - 1):
            self.nodes[i].left = None
            self.nodes[i].right = self.nodes[i + 1]


# @lc code=end
