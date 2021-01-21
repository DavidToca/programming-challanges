func twoSum(nums []int, target int) []int {
    var solution []int;
    
    for i:=0; i< len(nums) - 1; i++ {
        for j:=i+1; j< len(nums); j++ {
            if nums[i] + nums[j] == target{
                return []int{i, j}
            }
        }
    }
    return solution
}