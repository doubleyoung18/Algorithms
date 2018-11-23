def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    left = []
    right = []
    for i in range(n1):
        left.append(arr[low + i])
    for j in range(n2):
        right.append(arr[mid + j + 1])
    left.append(999999999)
    right.append(999999999)
    i, j = 0, 0
    for k in range(low, high + 1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

arr = [2, 5, 1, 4, 6]
merge_sort(arr, 0, len(arr) - 1)
print(arr)