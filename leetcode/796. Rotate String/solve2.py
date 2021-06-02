class Solution:
    def rotate(self, s):
        s += s[0]
        return s[1:]

    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        length = len(s)
        for step in range(length):
            s = self.rotate(s)
            if s == goal:
                return True

        return False