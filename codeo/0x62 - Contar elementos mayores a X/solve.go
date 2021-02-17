package main

import "fmt"

func main() {

	var n, cases, comp int

	fmt.Scanf("%d", &n)

	array := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &array[i])
	}

	fmt.Scanf("%d", &cases)

	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &array[i])
	}
}
