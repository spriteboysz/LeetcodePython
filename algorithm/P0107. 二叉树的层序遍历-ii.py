#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-28 23:16:43
LastEditTime: 2022-03-28 23:21:44
Description: 
FilePath: 107.二叉树的层序遍历-ii.py
"""
#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

from collections import deque
# @lc code=start
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        level, queue = [], deque()
        queue.append(root)
        while queue:
            curlevel = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curlevel.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level.append(curlevel)

        return level[::-1]

# @lc code=end
