class Solution:
    def rotate(self, A):
        A += A[0]
        return A[1:]

    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return True
        length = len(A)
        for step in range(length):
            A = self.rotate(A)
            if A == B:
                return True
        
        return False