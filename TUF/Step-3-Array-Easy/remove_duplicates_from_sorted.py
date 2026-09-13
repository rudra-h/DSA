class Solution:
    """def removeDuplicates(self, nums:list[int])->list[int]:
        n = len(nums)
        if n == 0 or n ==1:
            return nums
        
        result = []
        for i in range(n):
            if nums[i] not in result:
                result.append(nums[i])

        return result
        
        Time complexity: O(n^2)
        """
    
    def removeDuplicates(self, nums:list[int])->int:
        n = len(nums)
        if n == 0  or n ==1:
            return n
        
        i = 0 

        for j in range(1,n):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]

        return i+1


print(Solution().removeDuplicates([1,1,2]))
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
