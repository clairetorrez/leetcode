class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum  = 0
        running_sum = []
        for i in range(len(nums)):
            current_sum += nums[i]
            running_sum.append(current_sum)
        return running_sum