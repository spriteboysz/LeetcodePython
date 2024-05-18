#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-05-18 16:24
FileName: algorithm
Description:P0865. 具有所有最深节点的最小子树.py 
"""
from common.TreeNode import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return 0, None
            d1, lca1 = dfs(root.left)
            d2, lca2 = dfs(root.right)
            if d1 > d2:
                return d1 + 1, lca1
            if d1 < d2:
                return d2 + 1, lca2
            return d1 + 1, root

        _, lca = dfs(root)
        return lca


if __name__ == '__main__':
    root = TreeNode.create("[3,5,1,6,2,0,8,null,null,7,4]")
    print(Solution().subtreeWithAllDeepest(root))
