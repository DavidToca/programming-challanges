func findKthPositive(arr []int, k int) int {
	response := 0
	
	for i, j:= 0,0; k!=0; i++ {

		if j>=len(arr) || i != arr[j] {
			response = i
			k-=1
		} else {
			j+=1;
		}
	}
	return response
}