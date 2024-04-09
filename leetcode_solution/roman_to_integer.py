class Solution:

    def romanToInt(self, s: str) -> int:
        dicc_letter = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        suma = 0
        for i in range(len(s)):
            if i < len(s) - 1 and dicc_letter[s[i]] < dicc_letter[s[i + 1]]:
                suma -= dicc_letter[s[i]]
            else:
                suma += dicc_letter[s[i]]
        return suma
        
s = Solution()

print(s.romanToInt("MCMXCIV"))


# Other solutions

# def romanToInt(self, s: str) -> int:
#         dicc_letter = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
#         s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
#         suma = 0
#         for letter in s:
#             suma += dicc_letter[letter]
#         return suma