#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-28 22:59:57
LastEditTime: 2022-03-28 23:00:36
Description: 
FilePath: 103.二叉树的锯齿形层序遍历.py
"""
#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels, queue = [], deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)

        for j in range(len(levels)):
            if j % 2 == 1:
                levels[j] = levels[j][::-1]
        return levels

# @lc code=end
