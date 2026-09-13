class Union_arr:
    def union_arr(self, arr1:list[int], arr2:list[int]) -> list[int]:
        n1 = len(arr1)
        n2 = len(arr2)

        s1 = set(arr1)
        s2 = set(arr2)
        merged_set = s1 | s2
        return list(merged_set)
    
u1 = Union_arr()
print(u1.union_arr([10,5,20],[99,45,23]))