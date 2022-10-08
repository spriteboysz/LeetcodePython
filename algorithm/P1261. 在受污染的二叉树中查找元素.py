#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-03 21:40:05
LastEditTime: 2022-04-03 21:40:43
Description: 
FilePath: 1261.在受污染的二叉树中查找元素.py
"""
#
# @lc app=leetcode.cn id=1261 lang=python3
#
# [1261] 在受污染的二叉树中查找元素
#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()

        def dfs(node, val):
            if not node:
                return
            node.val = val
            self.values.add(val)
            dfs(node.left, val * 2 + 1)
            dfs(node.right, val * 2 + 2)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# @lc code=end
