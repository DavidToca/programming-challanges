class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        queue = []
        s_perm = str("0" * k)
        visited = {s_perm: True}
        queue.append(s_perm)

        while queue:
            s_perm = queue.pop(0)

            if s_perm not in s:
                return False

            for i in range(len(s_perm)):
                if s_perm[i] != "0":
                    continue
                new_perm = list(s_perm)
                new_perm[i] = "1"
                new_perm = ''.join(new_perm)
                if new_perm in visited:
                    continue
                queue.append(new_perm)
                visited[new_perm] = True
        return True