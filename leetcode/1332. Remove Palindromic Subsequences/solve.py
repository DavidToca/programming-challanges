class Solution:
    def is_palindrom(self, s):
        return s == s[::-1]

    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if self.is_palindrom(s):
            return 1
        return 2