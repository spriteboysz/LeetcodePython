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

# @lc code=start
from typing import List
from collections import deque

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

        for j in range(len(level)):
            if j % 2 == 1:
                level[j] = level[j][::-1]
        return level

# @lc code=end
