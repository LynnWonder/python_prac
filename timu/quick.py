# 练习分治算法：快排
# 快排的关键点是找到一个基准将一个数组分成两部分
# 两个子部分分别递归得到答案
# 最终将答案拼接起来，很明显这就是分治算法
# 时间复杂度：最好的情况下 O(nlogn) 最差的情况下选择的基准正好是每轮的最大值或者最小值：O(n2)
# 空间复杂度：存放基准值占用的空间 O(logn)
from typing import List


def quick_sort(ll: List, start: int, end: int) -> List:
    if len(ll) <= 1 or start >= end:
        return ll

    def partition(ll, start, end):
        # 原地移动
        # 选取一个基准值
        pivot_val, i = ll[end], start - 1
        for j in range(start, end):
            if ll[j] <= pivot_val:
                i += 1
                ll[i], ll[j] = ll[j], ll[i]
        ll[i + 1], ll[end] = ll[end], ll[i + 1]
        return i + 1

    pivot = partition(ll, start, end)
    quick_sort(ll, start, pivot - 1)
    quick_sort(ll, pivot + 1, end)
    return ll


if __name__ == "__main__":
    print(quick_sort([7, 4, 6, 5, 2, 3, 6], 0, 6))
    print(quick_sort([7, 20, 2, 15, 15, 7, 14, 4, 16, 11, 15, 18, 17, 1, 20, 6, 11, 3, 19, 9], 0, 19))
