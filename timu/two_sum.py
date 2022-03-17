class Solution:
    # def twoSum(self, nums, target):
    #     n = len(nums)
    #     for i in range(n):
    #         j = n - 1
    #         while j > i and nums[i] + nums[j] != target:
    #             j -= 1
    #         if j <= i:
    #             continue
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    def twoSum(self, nums, target):
        # 已知一个数，怎样高效率的在数组中寻找另一个数，那就是使用哈希表
        n = len(nums)
        table = {}
        for i in range(n):
            if target - nums[i] in table:
                return [i, table[target - nums[i]]]
            else:
                table[nums[i]] = i


test = Solution()

print(test.twoSum([2, 7, 11, 15], 9))
print(test.twoSum([3, 2, 4], 6))
