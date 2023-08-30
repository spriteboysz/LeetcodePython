#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-29 13:00
FileName: algorithm
Description:P1148. 文章浏览 I.py 
"""
import pandas as pd

from common.MySQL import get_sql_table


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['viewer_id'] == views['author_id']]['author_id'].drop_duplicates().sort_values()
    return pd.DataFrame({'id': df})


if __name__ == '__main__':
    view = get_sql_table('p1148', 'views')
    print(article_views(view))
