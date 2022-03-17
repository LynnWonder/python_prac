# https://leetcode-cn.com/problems/3sum/
# 三个数相加为 0, 取多个答案
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 不能有重复的答案

# 时间复杂度：O(N^2) 其中 N 是数组 nums 的长度。
# 空间复杂度：O(log N)。我们忽略存储答案的空间，额外的排序的空间复杂度为 O(logN)。
# 然而我们修改了输入的数组 nums，在实际情况下不一定允许，
# 因此也可以看成使用了一个额外的数组存储了 nums 的副本并进行排序，空间复杂度为 O(N)O(N)。
class Solution:
    # 快速排序的两个关键点：递归+就地排序
    def sort_nums(self, nums, start, end):
        def partition(nums, start, end) -> int:
            # 假设末尾为基准
            pivot = nums[end]
            pivot_index = end
            i = start - 1
            for j in range(start, end):
                # 总是寻找比基准值小的值
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            # 交换到基准该到的位置上去
            nums[i + 1], nums[pivot_index] = nums[pivot_index], nums[i + 1]
            return i + 1

        if start >= end:
            return nums
        # 找到基准
        pos = partition(nums, start, end)
        self.sort_nums(nums, start, pos - 1)
        self.sort_nums(nums, pos + 1, end)
        return nums

    def threeSum(self, nums):
        # 首先对数据进行排序，以防止出现重复的答案
        n = len(nums)
        nums = self.sort_nums(nums, 0, n - 1)
        res = []
        for i in range(0, n):
            # 首先在第一层循环这里我们知道 [-4, -1, -1, 0, 1, 2]
            # 在 以 -1 开头时必定造成重复答案，所以我们这样来处理一下
            # 跳过那些相等的值
            if i > 0 and nums[i] == nums[i-1]:
                continue
            z = n - 1
            for j in range(i + 1, n):
                # 我们加了一个 0 [-4, -1, -1, 0, 0, 1, 2]
                # 又出现了重复的内容  [-1, 0, 1], [-1, 0, 1]
                # 那我们也在这里加一个相同的限制，注意这里不再使用 j > 0
                # 我们只需要保证 j > i+1 即可，因为 i 最小是 0
                # j 不能从 0 或者 1 开始算
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while j < z and nums[j] + nums[z] > -nums[i]:
                    z -= 1
                if j >= z:
                    break
                if nums[j] + nums[z] == -nums[i]:
                    res.append([nums[i], nums[j], nums[z]])
        return res


# print(sort_nums([7, 4, 6, 5, 1, 3, 6], 0, 6))

a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4]))
print(a.threeSum([-1, 0, 1, 2, -1, -4, 0]))