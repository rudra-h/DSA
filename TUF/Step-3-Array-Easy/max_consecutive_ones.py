class Solution:
    def findMaxConsectiveOnes(self, nums:list[int])->int:
        n = len(nums)
        count = 0
        max_count = -1

        for i in range(n):
            if nums[i] == 1:
                count += 1
            elif nums[i]==0:
                max_count = max(max_count , count)
                count = 0

        ## if array ends with 1 then we need to check for max_count one more time because the last sequence of 1s might not be followed by a 0
        max_count = max(max_count , count)
        return max_count

mx = Solution().findMaxConsectiveOnes([1,0,1,1,0,1])
print(mx)
