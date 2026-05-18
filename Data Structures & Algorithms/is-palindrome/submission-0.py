class Solution:
    def isPalindrome(self, s: str) -> bool:
        split_str = "".join(char.lower() for char in s if char.isalnum())
        reversed_str = split_str[::-1]

        if split_str == reversed_str:
            return True
        
        return False