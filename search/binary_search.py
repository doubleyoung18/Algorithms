def binary_search(list, key):
    """二分查找
    Args：
    list:有序序列
    key:查找关键字
    return:
    mid：查找成功，返回元素索引；
    None:查找失败，返回空值
    """
    low = 0  # 左边界
    high = len(list)  # 右边界
    while low <= high:
        mid = (high - low) // 2  # 二分
        if list[mid] == key:
            return mid  # 查找成功，返回索引
        elif list[mid] > key:
            high = mid - 1  # 更新右边界，左搜
        else:
            low = mid + 1  # 更新左边界，右搜
    return None  # 查找失败，返回空值

list = [1, 2, 3, 4, 5, 6]
key = 3
result = binary_search(list, key)
print(result)