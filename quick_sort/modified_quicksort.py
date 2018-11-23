import time
import math
import random

# 分解
def partition(A, p, r):
    x = A[r]  # 主元
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

# 快排
def limited_quicksort(A, p, r, k):
    if p < r and r - p > k:
        q = partition(A, p, r)
        limited_quicksort(A, p, q-1, k)
        limited_quicksort(A, q+1, r, k)

# 快排优化
def modified_quicksort(A, p, r, k):
    limited_quicksort(A, p, r, k)
    insert_sort(A, p, r)

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q+1, r)

# 插入排序
def insert_sort(A, p, r):
    for i in range(p+1, r):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

if __name__ == "__main__":
    min_time = 9999  # 最小时间
    best_k = 0  # 最佳切分
    n = 1000  # 问题规模
    A0 = []
    for i in range(n):
        A0.append(random.randint(0, 100000))
    for round in range(n):
        A = A0.copy()
        print("排序序列：", A)
        k = round
        # if round != 2:
        #     k = random.randint(0, n)
        # else:
        #     k = int(math.sqrt(len(A)))
        start = time.clock()
        modified_quicksort(A, 0, len(A) - 1, k)
        end = time.clock()
        print("选取k:", k)
        runtime = end - start
        print("运行时间:", runtime)
        if runtime < min_time:
            min_time = runtime
            best_k = k
        print("排序结果:", A)
        print("----------")
    print("最佳k值:", best_k)
    print("最快时间", min_time)
    start = time.clock()
    quicksort(A, 0, len(A)-1)
    end = time.clock()
    runtime = end - start
    print("普通快排运行时间:", runtime)

    start = time.clock()
    A.sort()
    end = time.clock()
    runtime = end - start
    print("内建sort()运行时间:", runtime)
    # print(min_time / runtime)