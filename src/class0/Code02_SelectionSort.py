"""
@author: jackchen
选择排序法：
输入一个数据，通过选择排序法输出从小到大排好序的数组。以下为选择排序法：
1. 0~n-1,找到其中最小值，和数组第一个位置的数交换位置。
2. 1~n-1,找到其中最小值，和数组第二个位置的数交换位置
3. ...
注意：
1. 边界条件: 空数组，数组长度<=1, 无需排序
2.
"""


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr


def SelectionSort(arr):
    if (arr is None) or (len(arr) <= 1):
        return arr
    else:
        n = len(arr)
        for i in range(n):
            minValueIndex = i
            for j in range(i + 1, n):
                minValueIndex = j if arr[j] < arr[minValueIndex] else minValueIndex
                swap(arr, i, minValueIndex)
        return arr


if __name__ == '__main__':
    arr = SelectionSort([3, 2, 1, 4, 5, 7, 8])
    print(arr)
