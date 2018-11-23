"""快速排序"""
# 解决
def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q+1, r)

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

def quick_sort(arr, low, high):
    if(low >= high):
        return
    first = low
    last = high
    pivot = low  # 枢纽
    while first < last :
        while first < last and arr[last] >= arr[pivot]:
            last -= 1
        while first < last and arr[first] <= arr[pivot]:
            first += 1
        arr[first], arr[last] = arr[last], arr[first]
    arr[pivot], arr[first] = arr[first], arr[pivot]
    quick_sort(arr, low, first - 1)
    quick_sort(arr, first + 1, high)

if __name__ == "__main__":
    arr = list(map(int, input("输入待排序序列（以空格分隔）：").split(" ")))
    quicksort(arr, 0, len(arr) - 1)
    print("\n最终排序结果：", arr)