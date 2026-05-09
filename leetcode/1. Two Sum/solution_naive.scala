object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    var response:Array[Int] = Array.empty[Int]
    // iterate all nums with index
    for( (num, index) <- nums.zipWithIndex) {
        for ( (inner_num, inner_index) <- nums.zipWithIndex) {
            if(index != inner_index) then
                if (num + inner_num == target) then
                    response = Array[Int](index, inner_index)
        }

    }
    response
  }

}