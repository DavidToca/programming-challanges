class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        variation = False
        for digit in s:
            if variation and digit == '1':
                return False
            if digit != '1':
                variation = True
        return True