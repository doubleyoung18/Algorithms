#!/usr/bin/env/python
# -*- coding:utf-8 -*-

"""
@Author:Double Young
@Time:2018/12/16 15:45:54
@Desc:最佳调度问题（回溯法）
"""

min = float("inf")

def backtrack(depth, cost, count):
    """
    回溯求解最佳调度时间和方案
    :param depth: 搜索深度
    :param cost: 当前开销
    :return: 
    """
    # 涉及值修改，必须要在作用域内附加声明！
    global count
    global min
    global best
    count += 1
    if cost >= min:  # 上界剪枝1
        return
    if depth == n:  # 搜索至叶子结点
        if cost < min:
            min = cost
            best = dispatch[:]  # 深拷贝！
        return
    else:
        for i in range(k):
            machine[i] += time[depth]
            if machine[i] < min:  # 上界剪枝2
                dispatch[depth] = i+1
                backtrack(depth+1, max(cost, machine[i]), count)
            machine[i] -= time[depth]
    return

if __name__ == "__main__":
    # n, k = map(int, input().split())  # n个任务，k台机器
    # time = list(map(int, input().split()))  # 各个任务用时
    n, k = 7, 3  # n个任务，k台机器
    time = [2, 14, 4, 16, 6, 5, 3]  # 各个任务用时
    dispatch = [0] * n  # 当前调度方案
    machine = [0] * k  # 各机器用时
    min = float("inf")  # 最佳用时（初始化为无穷）
    best = []  # 最佳调度方案
    count = 0  # 递归次数
    backtrack(0, 0, 0)
    print("最佳调度时间：", min)
    print("方案递归次数：", count)
    print("最佳调度方案：", best)

    print("----------正序最佳调度----------")
    time.sort()
    min = float("inf")  # 最佳用时（初始化为无穷）
    best = []  # 最佳调度方案
    count = 0  # 递归次数
    backtrack(0, 0, 0)
    print("最佳调度时间：", min)
    print("方案递归次数：", count)
    print("最佳调度方案：", best)

    print("----------逆序最佳调度----------")
    time.sort(reverse=True)
    min = float("inf")  # 最佳用时（初始化为无穷）
    best = []  # 最佳调度方案
    count = 0  # 递归次数
    backtrack(0, 0, 0)
    print("最佳调度时间：", min)
    print("最佳调度方案：", best)
    print("方案递归次数：", count)