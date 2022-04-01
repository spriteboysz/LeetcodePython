#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-31 23:03:28
LastEditTime: 2022-03-31 23:03:51
Description: 
FilePath: 1457.二叉树中的伪回文路径.py
"""
#
# @lc app=leetcode.cn id=1457 lang=python3
#
# [1457] 二叉树中的伪回文路径
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque, Counter, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        queue = deque()
        queue.append((root, [root.val]))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                if self.check_path(path):
                    count += 1
            if node.left:
                queue.append((node.left, path + [node.left.val]))
            if node.right:
                queue.append((node.right, path + [node.right.val]))
        return count

    def check_path(self, path):
        hash_table = defaultdict(int)
        for i in path:
            hash_table[i] += 1

        odd_list = [value for value in hash_table.values() if value % 2 == 1]
        return len(odd_list) <= 1


# @lc code=end
