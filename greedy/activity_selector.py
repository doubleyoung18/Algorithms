#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@Author:Double Young
@Time:2018/11/26 10:35:04
@Desc:活动选择问题
"""

def recursive_activity_selector(s, f, k, n):
    """
    递归贪心算法(尾递归):O(n)
    :param s:活动开始时间序列
    :param f:活动结束时间序列
    :param k:当前最大兼容活动子集尾索引
    :param n:活动数
    :return:最大兼容活动子集A
    """
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        A = recursive_activity_selector(s, f, m, n)
        A.append(m)  # 注：list.append()返回NoneType
        return A
    else:
        return []

def greedy_activity_selector(s, f):
    """
    迭代贪心算法:O(n)
    :param s:活动开始时间序列
    :param f:活动结束时间序列
    :return:最大兼容活动子集A
    """
    n = len(s)  # 活动数
    A = []  # 解
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m
    return A


if __name__ == "__main__":
    n = 11
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6 ,7, 9, 9, 10, 11, 12, 14, 16]  # 按结束时间升序
    result1 = recursive_activity_selector(s, f, 0, n)
    result1.reverse()  # 递归逆序
    print(result1)
    result2 = greedy_activity_selector(s, f)
    print(result2)