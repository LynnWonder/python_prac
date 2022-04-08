# 接雨水 https://leetcode-cn.com/problems/trapping-rain-water/
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 输入：height = [4,2,0,3,2,5]
# 输出：9
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 当我们画出来图之后会知道从第一个元素 a 开始一直寻找到比它大的值 b 为止，用 a 去减凹进去的值就能得到答案
        # 当我们正向循环一次之后会发现这种算法无法拉取到像 4 2 3 这种情况存下来的雨水
        # 所以我们要反向再来一次
        # 再优化一下就是从左向右找到最大的，然后从右边向左一直到这个最大的收集的雨水就是题目要求的
        i, n, res = 0, len(height), 0
        t = n - 1
        while i < n - 1:
            pivot = height[i]
            for j in range(i + 1, n):
                if height[j] >= pivot:
                    break
            if height[j] >= pivot:
                res = res + sum(map(lambda x: pivot - x, height[i + 1:j]))
                i = j
            else:
                break
        while t > i:
            pivot = height[t]
            for z in range(t - 1, i-1, -1):
                if height[z] > pivot:
                    break
            if height[z] > pivot:
                res = res + sum(map(lambda x: pivot - x, height[z + 1: t]))
            t = z
        return res


if __name__ == "__main__":
    trap = Solution()
    print(trap.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap.trap([4, 2, 0, 3, 2, 5]))
    print(trap.trap([2, 0, 2]))
    print(trap.trap([4, 2, 3]))
    print(trap.trap([5, 5, 1, 7, 1, 1, 5, 2, 7, 6]))
