class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        original_x = x
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        return original_x == reversed_num
