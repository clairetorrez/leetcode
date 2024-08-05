# https://leetcode.com/problems/range-sum-query-immutable/
# difficulty: easy
# tags: prefix

# problem
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = []
        current_sum = 0
        for i in nums:
            current_sum += i
            self.sum.append(current_sum)

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sum[j]
        else:
            return self.sum[j] - self.sum[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
