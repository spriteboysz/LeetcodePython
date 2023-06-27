#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-19 14:21:37
LastEditTime: 2022-03-19 14:24:32
Description: 
FilePath: 1379.找出克隆二叉树中的相同节点.py
"""
from common.TreeNode import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        dic = dict()

        def preorder(cloned):
            if not cloned:
                return
            dic[cloned.val] = cloned
            preorder(cloned.left)
            preorder(cloned.right)

        preorder(cloned)
        return dic[target.val]
