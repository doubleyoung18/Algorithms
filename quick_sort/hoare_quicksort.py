"""Hoare划分快排"""
def hoare_quicksort(A, p, r):
    print(p, "::", r)
    if p < r:
        q = hoare_partition(A, p, r)
        hoare_quicksort(A, p, q-1)
        hoare_quicksort(A, q+1, r)

def hoare_partition(A, p, r):
    x = A[p]
    i = p - 1
    j = r + 1
    while True:
        while A[j] <= x:
            j += 1
        while A[i] >= x:
            i += 1
        if i < j:
            A[i], A[j] = A[j], A[i]
        else:
            return j

if __name__ == "__main__":
    arr = list(map(int, input("输入待排序序列（以空格分隔）：").split(" ")))
    hoare_quicksort(arr, 0, len(arr) - 1)
    print("\n最终排序结果：", arr)