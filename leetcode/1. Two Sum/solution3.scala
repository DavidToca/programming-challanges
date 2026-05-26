object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        var result = Array.empty[Int]

        nums.zipWithIndex.foreach { (num, indexa) =>
            nums.zipWithIndex.foreach { (numb, indexb) =>
                if indexa < indexb && num + numb == target then
                    result = Array(indexa, indexb)   
            }
        }
        result
    }
}