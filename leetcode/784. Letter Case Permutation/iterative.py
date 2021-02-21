class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = ['']
        for i in S:
            if i.isalpha():
                s, u = i.lower(), i.upper()
                n_ans = []
                for e in ans:
                    n_ans.append(e + s)
                    n_ans.append(e + u)
            else:
                n_ans = [e + i for e in ans]
            ans = n_ans
        return ans