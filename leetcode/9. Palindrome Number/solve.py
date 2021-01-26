class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1 = str(x)
        s2 = list(str(x))
        s2.reverse()
        s2 = "".join(s2)
        return s1 == s2
