"""
快速排序 — 面试手撕版

核心思想：分治
  1. 选一个基准元素 pivot
  2. 将数组分成两部分：左边 <= pivot，右边 > pivot（partition 操作）
  3. 递归排序左右两部分

时间复杂度：平均 O(n log n)，最坏 O(n²)（数组已有序时）
空间复杂度：O(log n) 递归栈深度（平均）
不稳定排序
"""

from random import randint


# ==================== partition 函数（面试重点）====================

def partition(arr, left, right):
    """Lomuto 分区方案 — 代码最简洁，面试首选

    思路：取最后一个元素为 pivot，维护指针 i，
          使得 arr[left..i-1] 都 <= pivot，arr[i..j-1] 都 > pivot
    """
    pivot = arr[right]  # 选最右元素为基准
    i = left            # i 指向"小于等于区"的末尾+1

    # 同向双指针
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # 把 pivot 放到正确位置
    arr[i], arr[right] = arr[right], arr[i]
    return i  # 返回 pivot 的最终位置


# ==================== 快速排序主函数 ====================

def quick_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return arr

    pivot_idx = partition(arr, left, right)
    quick_sort(arr, left, pivot_idx - 1)
    quick_sort(arr, pivot_idx + 1, right)

    return arr


# ==================== 随机化 pivot（避免最坏 O(n²)）====================

def partition_random(arr, left, right):
    """随机选 pivot，然后走 Lomuto 流程"""
    rand_idx = randint(left, right)
    arr[rand_idx], arr[right] = arr[right], arr[rand_idx]
    return partition(arr, left, right)


def quick_sort_random(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return arr

    p = partition_random(arr, left, right)
    quick_sort_random(arr, left, p - 1)
    quick_sort_random(arr, p + 1, right)

    return arr


# ==================== 测试 ====================

if __name__ == "__main__":
    test = [3, 6, 8, 10, 1, 2, 1]

    print("原始数组:   ", test)
    print("Lomuto 分区:", quick_sort(test[:]))
    print("随机化版本: ", quick_sort_random(test[:]))
