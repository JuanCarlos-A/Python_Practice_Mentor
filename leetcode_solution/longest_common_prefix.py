class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for i in range(len(strs)):
            if len(strs[i]) == 0:
                return ""
            if len(strs) == 1:
                return strs[0]
            if len(strs) == 0:
                return ""
            
        prefix = ""

        for i in range(len(min(strs))):
            letter = strs[0][i]

            for j in range(1, len(strs)):
                if strs[j][i] != letter:
                    return prefix
            prefix += letter

        return prefix
    
s = Solution()

print(s.longestCommonPrefix(["flower","flow","flight"]))





# Solucion obtenida de LeetCode Solutions

# def longestCommonPrefix(self, strs: list[str]) -> str:
#         if len(strs) == 1:
#             return strs[0]
        
#         common_length = len(strs[0])

#         for outer_index in range(1, len(strs)):
#             common_prefix_length = 0

#             common_length = min(common_length, len(strs[outer_index]))
#             for index in range(common_length):
#                 if strs[outer_index - 1][index] == strs[outer_index][index]:
#                     common_prefix_length += 1
#                 else:
#                     common_length = common_prefix_length
#                     break

#         return strs[0][:common_prefix_length]