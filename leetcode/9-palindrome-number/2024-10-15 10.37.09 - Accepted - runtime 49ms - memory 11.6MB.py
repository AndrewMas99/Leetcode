class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        # Single Digit numbers are palindromes
        if x < 10 & x > 0:
            return True
        
        # Convert the integer to a string and check if it's the same when reversed
        x_str = str(x)
        return x_str == x_str[::-1]
