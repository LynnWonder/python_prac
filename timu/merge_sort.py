# 归并排序
# 同样是使用分治算法
# 关键点是分成两部分，然后合并两个有序数组
# 时间复杂度计算方法 T(n) = 2T(n/2) + n   (第二个加数是合并的时候带来的时间复杂度) 计算后为 O(nlogn)
# 空间复杂度是存放结果的数组占用的空间 O(n)
from typing import List


def merge_sort(ll: List) -> List:
    if len(ll) <= 1:
        return ll
    split_num = int(len(ll) / 2)
    left = ll[:split_num]
    right = ll[split_num:]

    def merge_sorted(ll1, ll2):
        res = []
        while len(ll1) > 0 and len(ll2) > 0:
            if ll1[0] < ll2[0]:
                res.append(ll1.pop(0))
            else:
                res.append(ll2.pop(0))
        if len(ll1) > 0:
            res.extend(ll1)
        if len(ll2) > 0:
            res.extend(ll2)
        return res

    return merge_sorted(merge_sort(left), merge_sort(right))


if __name__ == "__main__":
    print(merge_sort([7, 4, 6, 5, 2, 3, 6]))
    print(merge_sort([7, 20, 2, 15, 15, 7, 14, 4, 16, 11, 15, 18, 17, 1, 20, 6, 11, 3, 19, 9]))