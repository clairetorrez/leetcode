# https://leetcode.com/problems/running-sum-of-1d-array/
# difficulty: easy
# tags: prefix

# problem
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Solution, O(n) time, O(1) space

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum  = 0
        running_sum = []
        for i in range(len(nums)):
            current_sum += nums[i]
            running_sum.append(current_sum)
        return running_sum
