#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2023-08-29 10:33
FileName: algorithm
Description:P1683. 无效的推文.py 
"""
import pandas as pd

from common.MySQL import get_sql_table


def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]


if __name__ == '__main__':
    tweets = get_sql_table('p1683', 'tweets')
    print(invalid_tweets(tweets))
