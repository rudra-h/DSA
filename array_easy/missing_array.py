class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = int((n*(n+1))/2)
        print(total_sum)
        arr_total_sum  = 0
        for num in nums:
            arr_total_sum +=num

        print(arr_total_sum)

        return total_sum - arr_total_sum

m1 = Solution()

result = m1.missingNumber([3,0,1])
        