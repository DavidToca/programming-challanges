object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val result: Array[Array[Int]] = for {
            (a, i) <- nums.zipWithIndex
            (b, j) <- nums.zipWithIndex
            if i < j && a + b == target
        } yield Array(i, j)
        result.head
    }
}