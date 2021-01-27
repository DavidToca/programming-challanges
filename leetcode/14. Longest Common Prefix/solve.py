class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""

        if(len(strs) == 1):
            return strs[0]

        words = [ list(word) for word in strs ]

        first_word = words[0]
        response = ""

        for i in range(len(first_word)):
            current_letter = first_word[i]

            for word in words:
                if i >= len(word):
                    return response
                if word[i] != current_letter:
                    return response
            
            response += current_letter
        
        return response