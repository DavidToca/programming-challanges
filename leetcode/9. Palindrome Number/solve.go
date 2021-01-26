func Reverse(a string) string{
    runes := []rune(a)
    reversed := make([]rune, len(a))
    
    j := 0
    
    for i:=len(a)-1;i>=0;i-- {
        reversed[j] = runes[i]
        j++
    }

    return string(reversed)
}

func isPalindrome(x int) bool {
    s1 := strconv.Itoa(x)
    
    return s1 == Reverse(s1)
}