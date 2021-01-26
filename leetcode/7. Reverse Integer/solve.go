const min_int = -2147483648;
const max_int = 2147483647;

func Reverse(a string) string {
	runes := []rune(a)
	reversed := make([]rune, len(a))
	j := 0
	for i := len(a) - 1; i >= 0; i-- {
		reversed[j] = runes[i]
		j++
	}
	return string(reversed)

}

func reverse(x int) int {
  	a := strconv.Itoa(x)
	runes := []rune(a)
	sign := string(runes[0]) == "-"
	if sign {
		a = string(runes[1:])

	}

	a = Reverse(a)
	if sign {
		a = "-" + a
	}

	response, _ := strconv.Atoi(a)
	
	if response >=min_int && response <=max_int {
		return response
	} else{
		return 0
	}  
}

