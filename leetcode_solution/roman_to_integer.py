class Solution:

    def romanToInt(self, s: str) -> int:
        dicc_letter = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        suma = 0
        for letter in s:
            suma += dicc_letter[letter]
        return suma
        
s = Solution()

print(s.romanToInt("MCMXCIV"))