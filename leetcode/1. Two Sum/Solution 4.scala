object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val numsWithIndex = nums.zipWithIndex
        (for
            (a, i) <- numsWithIndex.iterator
            (b, j) <- numsWithIndex.iterator
            if i < j && a+b==target
        yield Array(i,j)
        ).nextOption.getOrElse(Array())
    }
}