class Solution:
    def leftRotateByOne(self, arr:list[int],x:int)->list[int]:
        n = len(arr)
        if n ==0 or n ==1:
            return arr
        
        result = [0]*n
        for i in range(n):
            result[(i-x+n)%n] = arr[i]
        return result
    
    def rightRotateByOne(self, arr:list[int],x:int)->list[int]:
        n = len(arr)
        if n ==0 or n ==1:
            return arr
        
        result = [0]*n
        for i in range(n):
            result[(i+x+n)%n] = arr[i]
        return result
    
print(Solution().leftRotateByOne([1,2,3,4,5],1))
print(Solution().leftRotateByOne([3,7,8,9,10,11],3))
print(Solution().rightRotateByOne([1,2,3,4,5,6,7],2))