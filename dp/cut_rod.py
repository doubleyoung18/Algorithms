"""
钢条切割问题
给定一段长度为n英寸的钢条和一个价格表pi(i=1,2,...,n)，
求钢条切割方案，使得销售收益rn最大。
"""

NEGATIVE_INFINITY = -999999999  # -∞

def cut_rod(price, length):
    """
    自顶向下递归求最大收益
    :param price:价格
    :param length:长度
    :return:
        q:最大收益
    """
    if length == 0:
        return 0
    else:
        q = NEGATIVE_INFINITY
        for i in range(1, length+1):
            q = max(q, price[i-1] + cut_rod(price, length-i))
        return q

# 自顶向下动态规划求最大收益（初始化）
def top_down_cut_rod(length, price):
    receipts = [NEGATIVE_INFINITY] * (length + 1)
    # solution = [0] * (length + 1)
    return top_down_cut_rod_aux(length, price, receipts)

# 自顶向下动态规划求最大收益
def top_down_cut_rod_aux(length, price, receipts):
    if receipts[length-1] >= 0:
        return receipts[length-1]
    if length == 0:
        q = 0
    else:
        q = NEGATIVE_INFINITY
        for i in range(1, length+1):
            if q < price[i-1] + top_down_cut_rod_aux(length-i, price, receipts):
                q = price[i-1] + top_down_cut_rod_aux(length-i, price, receipts)
        receipts[length-1] = q
    return q

# 自底向上动态规划求最大收益（并记录切割方案）
def bottom_up_cut_rod(length, price):
    receipts = [0] * (length + 1)
    solution = [0] * (length + 1)
    for i in range(1, length+1):
        q = NEGATIVE_INFINITY
        for j in range(1, i+1):
            if q < price[j-1] + receipts[i-j]:
                q = price[j-1] + receipts[i-j]
                solution[i] = j
                receipts[i] = q
    return receipts, solution

price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
length = int(input("输入要切割的钢条长度（1-10）："))
receipt = cut_rod(price, length)
print("递归求得的最大收益：%.2f" % receipt)
receipt = top_down_cut_rod(length, price)
print("自顶向下动态规划求得的最大收益：%.2f" % receipt)
(receipts, solution) = bottom_up_cut_rod(length, price)
print("自底向上动态规划求得的最大收益：%.2f" % receipts[length])
print("最大收益：", receipts)
print("切割方案：", solution)