#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-07 23:41:03
LastEditTime: 2022-03-07 23:45:24
Description: 
FilePath: 501.二叉搜索树中的众数.py
"""

from collections import defaultdict
from typing import List

from common.TreeNode import TreeNode


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dic[node.val] += 1
            dfs(node.right)

        dic = defaultdict(int)
        dfs(root)
        maxvalue = []
        _, maximum = max(dic.items(), key=lambda el: el[1])
        for k, v in filter(lambda el: el[1] == maximum, dic.items()):
            maxvalue.append(int(k))
        return maxvalue
