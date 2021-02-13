package main

import "fmt"

func main() {

	var n int

	fmt.Scanf("%d", &n)
	a := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &a[i])
	}

	lastnumber := a[0]
	for i := 1; i < n; i++ {
		if lastnumber > a[i] {
			fmt.Println("Desordenado")
			return
		}
		lastnumber = a[i]
	}
	fmt.Println("Ordenado")
}
