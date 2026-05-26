object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        var numsInMap = Map.empty[Int, Int]

        var result = Array.empty[Int]

        for (a, i) <- nums.zipWithIndex
        do
            numsInMap = numsInMap + (a -> i)
        
        for (a, i) <- nums.zipWithIndex
        do
            val diff = target-a
            if numsInMap.contains(diff) && numsInMap(diff) > i then
                result = Array(i, numsInMap(diff))
        
        result

    }
}