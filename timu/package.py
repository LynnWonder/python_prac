# 问题：给定 n 种物品和一背包。
# 物品 i 的重量是 wi，其价值为 pi，背包的容量为 C。问应如何选择装入背包的物品，使得装入背包中物品的总价值最大?
# 注意每种物品只能放进去 0 或 1 次
# 我们通过观察可以发现，取容量为 c 的背包的最大价值时，在 0-1 问题上它只有可能包含某个物品或者不包含某个物品，与此同时假如包含这个物品，那么
# F(c-wi) 势必是最大的，也就是符合最优子结构特点即局部最优解能够得到全局最优解所以我们直接可以来自底向上的解决
# F(c, arr) = max(F(c-wi, arr1)+pi, F(c,arr1))   其中 arr1 不包含 i 这个物品
# 确定边界：F(0, arr) = 0，同时对 arr 长度为 1 的情况进行比较处理
# TIP 经过学习之后会发现其实没必要将所有元素遍历一次，我们只需要知道 F(c,arr) = max(F(c-wi, arr[:i])+pi, F(c,arr[:i)) 即可
# 思考是否需要暂存值
# 我们发现使用动态规划可以利用二维数组对结果值进行暂存
from typing import List


def package(w: List[int], p: List[int], c: int) -> int:
    n = len(w)
    if c <= 0 or n <= 0:
        return 0
    else:
        # for i in range(n):
        #     tmp_w, tmp_p = w[:i], p[:i]
        #     tmp_w.extend(w[i + 1:])
        #     tmp_p.extend(p[i + 1:])
        #     a = package(tmp_w, tmp_p, c - w[i]) + p[i] if c - w[i] >= 0 else 0
        #     res = max(res, a, package(tmp_w, tmp_p, c))
        # 不再是用循环比较，而是通过如下方式
        # a = package(w[:n - 1], p[:n - 1], c - w[n - 1]) + p[n - 1] if c - w[n - 1] >= 0 else 0
        # res = max(a, package(w[:n - 1], p[:n - 1], c))
        # return res
        res = [[]]*n
        for i in range(n):
            res[i] = [0] * (c + 1)
        for j in range(c + 1):
            res[0][j] = p[0] if w[0] <= j else 0
        for i in range(1, n):
            for j in range(0, c + 1):
                res[i][j] = res[i-1][j]
                if j >= w[i]:
                    res[i][j] = max(res[i][j], res[i-1][j-w[i]]+p[i])
        return res[n-1][c]


if __name__ == "__main__":
    # print(package([1, 2], [4, 5], 2))
    print(package([1, 2], [4, 5], 1))
    print(package([1, 2], [4, 5], 2))


