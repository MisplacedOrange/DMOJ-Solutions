class Solution:
    def isPalindrome(self, x: int) -> bool:
        og = x
        palindrome = 0
        if x < 0:
            return False
        while x > 0:
            palindrome = palindrome * 10 + x % 10
            x //= 10
        
        if palindrome == og:
            return True
        else:
            return False