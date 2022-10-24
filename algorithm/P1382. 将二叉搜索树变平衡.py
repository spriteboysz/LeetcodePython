#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-10-24 23:36
FileName: algorithm/P1382. 将二叉搜索树变平衡.py
Description: 
"""
from common.TreeNode import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            values.append(root.val)
            dfs(root.right)

        def create(data):
            if len(data) == 0:
                return
            mid = len(data) >> 1
            root = TreeNode(data[mid])
            root.left = create(data[:mid])
            root.right = create(data[mid + 1:])
            return root

        dfs(root)
        return create(values)


if __name__ == '__main__':
    root = TreeNode().create("[1,null,2,null,3,null,4,null,null]")
    solution = Solution().balanceBST(root)
    print(solution)
