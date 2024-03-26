""" Problem: Palindrome Number """
#Solution 1
# class Solution:
#     """ Solution Class"""
#     def is_palindrome(self, x: int) -> bool:
#        """ is_palindrome Method"""
#         num_origin = x
#         num_invert = 0
#         while x > 0:
#             num = x % 10
#             num_invert = (num_invert * 10) + num
#             x //= 10
#         return num_origin == num_invert


#Solution 2
class Solution:
    """ Solution Class"""
    def is_palindrome(self, x: int) -> bool:
        """ is_palindrome Method"""
        return str(x)[::-1] == str(x)

print(Solution().is_palindrome(121))
