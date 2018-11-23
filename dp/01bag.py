def dp_bag(n, c, v, w):
    m = [[0 for col in range(c + 1)] for row in range(n + 1)]  # 背包选择记录表
    book = [0] * n
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if j < w[i]:  # 若背包重量小于等于第i个物品重量
                m[i][j] = m[i - 1][j]  # 不放入该物品
            else:  # 若背包重量大于第i个物品重量
                m[i][j] = max(m[i - 1][j], m[i - 1][j - w[i]] + v[i])
    print("最大收益：", m[n][c])

    print("最大收益记录表：（m[i][j]-背包重量为j时考虑第i个物品时的最大收益）")
    for i in range(1, n+1):
        for j in range(1, c+1):
            print(m[i][j], end="\t")
        print()

    for i in range(n, 0, -1):
        if m[i][c] == m[i-1][c]:
            book[i-1] = 0
        else:
            book[i-1] = 1
            c -= w[i]

    print("拿去方案记录表：（1-拿；0-不拿）")
    print(book)

n = 6  # 可选物品数
c = 12  # 背包总重量
v = [0, 8, 10, 6, 3, 7, 2]  # 可选物品价值
w = [0, 4, 6, 2, 2, 5, 1]  # 可选物品重量
dp_bag(n, c, v, w)