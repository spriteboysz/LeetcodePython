#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-16 23:54:52
LastEditTime: 2022-02-17 00:01:14
Description: 
FilePath: 94.二叉树的中序遍历.py
"""
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return (
                    self.inorderTraversal(root.left)
                    + [root.val]
                    + self.inorderTraversal(root.right)
            )

# @lc code=end
