# 部分背包问题
# 给定一个最大载重量为 c 的卡车和 n 种食品，有食盐、白糖、大米等。
# 已知第 i 种食品最多，拥有 Wi 千克，其商品价值为 vi 元/千克，
# 编程确定一种装货方案，使得装入背包中的所有物品总价值最大。
#
# 特点：这些物品都是可以任意装下的。

# 和 0-1 背包问题不一样的是，0-1 背包是要么装这个物品要么不装这个物品，部分背包则是可以装多个这个物品
# 为了让价值最大，我们肯定优先装价值高（性价比高即单价高）的物品，可以说是一种贪心算法
# 时间复杂度：O(N)
# 空间复杂度：O(NC) 用了一个新数组来暂存和排序



from typing import List


def part_package(w: List[int], v: List[int], c: int) -> float:
    n, ans = len(w), 0
    res = [[]] * n
    # 首先按单价排序
    for i in range(n):
        res[i] = [w[i], v[i]]
    res.sort(key=lambda val: val[1], reverse=True)
    # 如果 v 标识的是总价不是单价，那么其实还是按单价排序
    # res.sort(key=lambda val: float(val[1] / val[0]) if val[0] != 0 else 0, reverse=True)
    print(res)
    for val in res:
        if c == 0:
            return ans
        if val[0] <= c:
            c = c - val[0]
            ans += val[1] * val[0]
            # 如果 v 标识的是总价不是单价，那么其实还是按单价排序
            # ans += val[1]
        else:
            # 如果 v 标识的是总价不是单价，那么其实还是按单价排序
            ans += val[1] * c
            # ans += float(float(val[1] / val[0]) * c)
            c = 0
    return ans


if __name__ == "__main__":
    print(part_package([1, 2, 3], [4, 5, 2], 5))
    # print(part_package([17, 30, 25, 41, 80, 70, 64, 56, 47, 38],
    #                    [50, 60, 70, 80, 90, 80, 70, 60, 50, 40],
    #                    120))
    # print(part_package([0, 10, 20, 30], [0, 60, 100, 120], 50))
