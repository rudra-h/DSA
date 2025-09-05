class Solution:
    def minimumRecolors(self, blocks:str, k:int) -> int:
        n = len(blocks)
        white_count = blocks[:k].count("W")
        min_recolors = white_count

        for i in range(k,n):
            if blocks[i] == "W":
                white_count +=1
            if blocks[i-k] == "W":
                white_count -=1
            min_recolors = min(min_recolors, white_count)

        return min_recolors
    

recolors = Solution().minimumRecolors("BWWWBB",6)
print(recolors)
                                      