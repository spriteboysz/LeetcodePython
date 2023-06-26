#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 22:11:14
LastEditTime: 2022-04-05 22:11:39
Description: 
FilePath: 297.二叉树的序列化与反序列化.py
"""
from common.TreeNode import TreeNode


#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        return (
            str(root.val)
            + ","
            + str(self.serialize(root.left))
            + ","
            + str(self.serialize(root.right))
        )

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def dfs(dataList):
            val = dataList.pop(0)
            if val == "None":
                return None
            root = TreeNode(int(val))
            root.left = dfs(dataList)
            root.right = dfs(dataList)
            return root

        dataList = data.split(",")
        return dfs(dataList)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
