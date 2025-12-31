class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lword = ""
        length = 0
        for char in s.strip():
            if char != ' ':
                lword += char
            elif char == ' ':
                lword = ""
        for char in lword:
            length += 1        
        return length