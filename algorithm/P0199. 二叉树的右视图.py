#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-27 23:00:29
LastEditTime: 2022-03-27 23:05:10
Description: 
FilePath: 199.二叉树的右视图.py
"""
#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue, res = [root], []
        while queue:
            res.append(queue[-1].val)
            curlevel = []
            for node in queue:
                if node.left:
                    curlevel.append(node.left)
                if node.right:
                    curlevel.append(node.right)
            queue = curlevel
        return res

# @lc code=end
