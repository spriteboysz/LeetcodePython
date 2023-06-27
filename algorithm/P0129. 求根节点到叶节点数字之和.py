#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-22 23:29:04
LastEditTime: 2022-03-22 23:33:16
Description: 
FilePath: 129.求根节点到叶节点数字之和.py
"""


#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, cur):
            if not node:
                return
            if not node.left and not node.right:
                return int(cur + str(node.val))

            left = dfs(node.left, cur + str(node.val)) if node.left else 0
            right = dfs(node.right, cur + str(node.val)) if node.right else 0
            print(left, right)
            return left + right

        return dfs(root, "")

# @lc code=end
