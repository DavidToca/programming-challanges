object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        var result = Array[Int]()
        for (num, indexa) <- nums.zipWithIndex
        do
            for (numb, indexb) <- nums.zipWithIndex 
            do
                if indexa < indexb && num + numb == target then
                  result = Array(indexa, indexb)
        result
    }
}