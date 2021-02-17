class Solution:

    def gen_options(self, character):
        if character.isnumeric():
            return [character]
        
        if character.isupper():
            return [character, character.lower()]
        return [character, character.upper()]
    
    def solve(self, word, position, full_word):
        if len(word) == len(full_word):
            return [word]
        permutations = []
        options = self.gen_options(full_word[position])
        
        for option in options:
            current_perm = self.solve(word+option, position+1, full_word)
            permutations.extend(current_perm)
        return permutations
        
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return S
        
        return self.solve("",0,  S)