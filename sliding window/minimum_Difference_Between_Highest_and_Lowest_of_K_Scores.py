class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:

        nums.sort()
        n = len(nums)
        start = 0
        end = k - 1

        min_diff = nums[end] - nums[start]
        for i in range(1,n-k+1):
            start += 1
            end += 1
            current_diff = nums[end] - nums[start]
            min_diff = min(min_diff, current_diff)
            

        return min_diff
        







