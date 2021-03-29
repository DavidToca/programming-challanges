class Solution:
    def originalDigits(self, s: str) -> str:

        result = []

        while s:

            letters = [
                {'letter': 'z', 'word': 'zero', 'response': 0},
                {'letter': 'g', 'word': 'eighth', 'response': 8},
                {'letter': 'u', 'word': 'four', 'response': 4},
                {'letter': 'x', 'word': 'six', 'response': 6},
                {'letter': 's', 'word': 'seven', 'response': 7},
                {'letter': 'v', 'word': 'five', 'response': 5},
                {'letter': 'i', 'word': 'nine', 'response': 9},
                {'letter': 'r', 'word': 'three', 'response': 3},
                {'letter': 'w', 'word': 'two', 'response': 2},
                {'letter': 'o', 'word': 'one', 'response': 1},
            ]

            for l in letters:
                if l['letter'] in s:
                    result.append(l['response'])

                    for i in l['word']:
                        s = s.replace(i, "", 1)

                    break

        result.sort()
        result = list(map(str, result))
        return ''.join(result)
