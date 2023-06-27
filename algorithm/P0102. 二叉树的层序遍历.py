#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-27 22:45:01
LastEditTime: 2022-03-27 22:52:43
Description: 
FilePath: 102.二叉树的层序遍历.py
"""
#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]  # 根节点入queue
        res = []
        while queue:
            res.append([node.val for node in queue])
            curlevel = []  # 存储当前层的孩子节点列表
            for node in queue:
                if node.left:  # 如果左子节点存在，入队列
                    curlevel.append(node.left)
                if node.right:
                    curlevel.append(node.right)
            queue = curlevel  # 把queue更新成下一层的结点
        return res

# @lc code=end
