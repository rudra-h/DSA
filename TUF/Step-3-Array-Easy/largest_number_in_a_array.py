## Problem Statement: Given an array, we have to find the largest element in the array
"""
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 
 """


class Solution:
    def LargestNumber(self,arr:list[int])-> int:
        n = len(arr)
        Largest = arr[0]

        for i in range(1,n):
            if arr[i] > Largest:
                Largest = arr[i]
        return Largest
    

Lagest = Solution()
print(Lagest.LargestNumber([2,5,1,3,0]))
print(Lagest.LargestNumber([8,10,5,7,9]))



 