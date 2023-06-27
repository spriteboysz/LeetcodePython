#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-02-17 00:08:36
LastEditTime: 2022-02-17 00:10:17
Description: 
FilePath: 145.二叉树的后序遍历.py
"""
#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        else:
            return (
                    self.postorderTraversal(root.left)
                    + self.postorderTraversal(root.right)
                    + [root.val]
            )

# @lc code=end
