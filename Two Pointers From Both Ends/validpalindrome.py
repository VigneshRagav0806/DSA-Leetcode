class Solution:
    def isPalindrome(s):
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True

"""
This method used two pointers to traverse any string having special characters or not
if the character encountered by the pointers is not an alpha numeric character, the pointer skips it and then compares characters.
It is not case sensitive, hence the characters are free to be converted to lowercase
If all characters match return True, else False
"""