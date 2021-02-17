class Solution:
    def letterCasePermutation(self, S):
        return map(''.join, product(*[set([i.lower(), i.upper()]) for i in S]))