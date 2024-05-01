#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-04-28 22:19
FileName: algorithm
Description:P1123. 最深叶节点的最近公共祖先.py 
"""
from typing import Optional

from common.TreeNode import TreeNode


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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

        return dfs(root)[1]


if __name__ == '__main__':
    print(Solution().lcaDeepestLeaves(TreeNode.create("[3,5,1,6,2,0,8,null,null,7,4]")))
