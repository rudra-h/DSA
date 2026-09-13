'''
Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

Example 2:
Input: N = 5, array[] = {5,4,6,7,8}
Output: False.
Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.
'''

class Solution:
    def isSorted(self, nums:list[int])->bool:
        n = len(nums)
        if n == 0 or n == 1:
            return True
              
        for i in range(n-1):
            if nums[i+1] - nums[i] < 0:
                return False
        return True
    
print(Solution().isSorted([1,2,3,4,5]))
print(Solution().isSorted([5,4,6,7,8]))
print(Solution().isSorted([1]))
print(Solution().isSorted([-3,-2,-5,-1]))
print(Solution().isSorted([2,2,2,2]))



'''
ANALYSIS: could have thought simply checking adjacent elements to determine if current element shall be greater than or equal to previous element. If any such instance found, return True. Else return false at end.
'''