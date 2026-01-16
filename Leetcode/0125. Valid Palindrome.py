class Solution:
    def isPalindrome(self, s: str) -> bool:

        palindrome = (''.join(char for char in s if char.isalpha() or char.isnumeric())).lower()
        return palindrome == palindrome[::-1]
    