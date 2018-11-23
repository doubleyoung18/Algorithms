def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for col in range(n)] for row in range(m)]  # LCS字符记录表
    c = [[0 for col in range(n)] for row in range(m)]  # LCS长度记录表
    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = '↖'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '↑'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = '←'
    return b, c

def print_lcs(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == '↖':
        print_lcs(b, X, i-1, j-1)
        print(X[i], end="")  # 输出
    elif b[i][j] == '↑':
        print_lcs(b, X, i-1, j)  # 向上找
    else:
        print_lcs(b, X, i, j-1)  # 向左找

def print_table(X, Y, table):
    print("  ", end="")
    for j in range(len(Y)):
        print(Y[j], end=" ")
    print("  ")
    for i in range(len(X)):
        print(X[i], end=" ")
        for j in range(len(Y)):
            print(table[i][j], end=" ")
        print()

X = input("请输入序列A：")
Y = input("请输入序列B：")
(b, c) = lcs_length(X, Y)
print("LCS：", end="")
print_lcs(b, X, len(X)-1, len(Y)-1)  # 从右下开始搜索

print()
print("LCS字符记录表b：")
print_table(X, Y, b)

print("LCS长度记录表c：")
print_table(X, Y, c)