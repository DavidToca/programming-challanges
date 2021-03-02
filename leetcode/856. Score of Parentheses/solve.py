class Solution:
    def scoreOfParentheses(self, S: str) -> int:

        S = S.replace('()', '|')

        queue = []
        response = 0
        for character in S:

            if character == '(':
                queue.append('(')
            elif character == '|':
                if not queue:
                    response += 1
                else:
                    response += 2 ** len(queue)
            else:
                queue.pop()
        return response