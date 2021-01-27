
func Split(strs []string) [][]rune {
	response := make([][]rune, len(strs))
	for i := 0; i < len(strs); i++ {
		runes := []rune(strs[i])
		response[i] = runes
	}
	return response
}

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	if len(strs) == 1 {
		return strs[0]
	}

	words := Split(strs)

	first_word := words[0]

	response := ""

	for i := 0; i < len(first_word); i++ {
		letter := first_word[i]

		for j := 1; j < len(words); j++ {
			if i >= len(words[j]) {
				return response
			}

			if letter != words[j][i] {
				return response
			}
		}
		response = response + string(letter)

	}

	return response
}
