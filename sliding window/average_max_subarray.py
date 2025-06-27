
class Solution:
    def findMaxAverage(self, nums:list[int], k:int) -> float:
        window_sum = sum(nums[:k])  # sum of first 'k' elements
        max_avg = window_sum / k  # max initial average

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            curr_avg = window_sum / k 
            max_avg = max(max_avg, curr_avg)

        return max_avg
    
max_average = Solution().findMaxAverage([1, 12, -5, -6, 50, 3], 4)
print(max_average)  # Output: 12.75


            

