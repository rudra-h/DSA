class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0 
        right = 0
        max_length = 0
        current_sum = 0

        while right < n : 
            current_sum += nums[right]

            while current_sum > k and left <= right:
                current_sum -= nums[left]
                left+=1

            if current_sum == k:
                max_length = max(max_length , right - left + 1)
            right+=1
        return max_length


ls = Solution().longestSubarray([1,2,3,4,5], 9)
print(ls)
