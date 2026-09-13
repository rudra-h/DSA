## Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
"""
Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present
"""

class Solution:
    def secondLargestNumber(self, arr:list[int])-> float:
        n = len(arr)
        if n < 2:
            return -1

        largest = arr[0]
        second_largest = float('-inf')

        for i in range(1,n):
            if arr[i]>largest:
                second_largest = largest
                largest = arr[i]
            elif arr[i] < largest :
                if arr[i] > second_largest:
                    second_largest = arr[i]

        if largest == second_largest or second_largest == float('-inf'):
            return -1
        
        return second_largest

second_largest = Solution()
print(second_largest.secondLargestNumber([1,2,4,7,7,5]))
print(second_largest.secondLargestNumber([8,1,2,4,3,9,5]))
print(second_largest.secondLargestNumber([1]))
print(second_largest.secondLargestNumber([2,2,2]))
print(second_largest.secondLargestNumber([-1,-2,-3 ]))