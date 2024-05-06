class Solution:
    def isValid(self, s: str) -> bool:
        dicc = {
            "}" : "{",
            ")" : "(",
            "]" : "["
            }
        
        lista = []
        
        for caracter in s:
            if caracter in dicc.values():
                lista.append(caracter)
            elif caracter in dicc.keys():
                if not lista or dicc[caracter] != lista.pop():
                    return False
            
        return not lista


solution = Solution()

print(solution.isValid("[]"))



# Otra Solucion Posible
# class Solution:
#     def isValid(self, s: str) -> bool:
#         dicc = {
#             "}" : "{",
#             ")" : "(",
#             "]" : "["
#             }
        
#         lista = []
        
#         for caracter in s:
#             if caracter in dicc.values():
#                 lista.append(caracter)
#             elif lista and dicc[caracter] == lista[-1]:
#                 lista.pop()
#             else:
#                 return False
            
#         return not lista
