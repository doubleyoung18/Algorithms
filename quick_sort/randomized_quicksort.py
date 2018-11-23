"""随机化快排"""
from random import randint

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_partition(A, p, q-1)
        randomized_partition(A, q+1, r)

def randomized_partition(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)

def partition(A, p, r):
    x = A[r]  # 主元
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

if __name__ == "__main__":
    arr = list(map(int, input("输入待排序序列（以空格分隔）：").split(" ")))
    randomized_quicksort(arr, 0, len(arr) - 1)
    print("\n最终排序结果：", arr)
