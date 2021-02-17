package main

import "fmt"

func main() {

	var n, cases, p, q int

	fmt.Scanf("%d", &n)

	array := make([]int, n)

	total := 0
	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &array[i])
		total += array[i]
		array[i] = total
	}

	fmt.Scanf("%d", &cases)

	for i := 0; i < cases; i++ {
		fmt.Scanf("%d", &p)
		fmt.Scanf("%d", &q)
		if p == 0 {
			fmt.Println(array[q])
		} else {
			fmt.Println(array[q] - array[p-1])
		}
	}

}
