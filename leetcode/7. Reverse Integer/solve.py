class Solution:
    def reverse(self, x: int) -> int:
        min_int = -(2**31)
        max_int = 2**31 - 1
        
        a = str(x)
        
        sign = ""
        
        if a.startswith("-"):
            sign = "-"
            a = a[1:]
        
        a = a[::-1]
        a = f"{sign}{a}"
        
        a = int(a)
        
        if min_int <= a <= max_int:
            return a
        return 0
        
