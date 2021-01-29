class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        brackets = {
            ')': '(',
            '}': '{', 
            ']': '[',
        }
        
        for char in list(s):
            if char not in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                
                if brackets[char] != top:
                    return False
        return len(stack) == 0