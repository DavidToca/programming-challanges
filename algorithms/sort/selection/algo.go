package main

import "fmt"

func main() {
	var n int
	fmt.Scanf("%d", n)

	arr := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &arr[i])
	}

}
