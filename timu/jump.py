# 跳跃游戏 II https://leetcode-cn.com/problems/jump-game-ii/
# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少地跳跃次数到达数组的最后一个位置。
#
# 假设你总是可以到达数组的最后一个位置。
#

# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#

# 输入: nums = [2,3,0,1,4]
# 输出: 2
from typing import List


class Solution:
    # 这个题可以用贪心算法来解决，就是每次都往最远的距离跳
    def jump(self, nums: List[int]) -> int:
        n, max_pos, end, step = len(nums), 0, 0, 0
        for i in range(n-1):
            # 但是我们知道了每个元素上最远能跳到的位置之后，怎么收集 step 呢
            max_pos = max(max_pos, nums[i] + i)
            # 只能每次跳到最远位置之后呢就加一步，但是循环应该到 n-1 就停止
            if i == end:
                end = max_pos
                step += 1
        return step


if __name__ == "__main__":
    jump = Solution()
    # print(jump.jump([1, 1, 1, 1]))
    # print(jump.jump([1]))
    # 以这个测试用例为例讲讲跳转过程
    # end max_pos  step
    #  0    5       0
    #  5    10      1
    #  10   10      2
    #  10   11(3+8) 2
    #  11   11      3
    print(jump.jump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))
