# 1876. Substrings of Size Three with Distinct Characters (Easy)
# A string is good if it has no repeated characters.
# Return the number of good substrings of length 3 in a given string s.

# Example 1:
# Input: "xyzzaz" → Substrings: ["xyz", "yzz", "zza", "zaz"]
# Output: 1 ("xyz" is the only good substring)

# Example 2:
# Input: "aababcabc" → Substrings: ["aab", "aba", "bab", "abc", "bca", "cab", "abc"]
# Output: 4 (Good substrings: "abc", "bca", "cab", "abc")


class Solution:
    def countGoodSubstrings(self, s:str) -> int:
        n = len(s)
        if n < 3 :
            return 0
        start = 0
        end = 2
        count = 0
        for i in range(n-2):
            check_set = set()
            for ch in s[start:end+1]:
                check_set.add(ch)

            if len(check_set) == 3:
                count += 1

            start+=1
            end+=1
        return count
    
result= Solution().countGoodSubstrings("aababcabc")
print(result)  # Output: 1

            
        