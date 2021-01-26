
func romanToInt(s string) int {
    equivalence := map[rune]int {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}
	runes := []rune(s)
	last_numb := -1
    response := 0
	for i:=len(s)-1; i>=0; i-- {
        roman := equivalence[runes[i]]
		if(last_numb > roman){
			response -= roman
		} else {
			response += roman
		}
        last_numb = roman
	}
	return response
}