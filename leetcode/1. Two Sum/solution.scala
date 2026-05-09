object Solution {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    var response:Array[Int] = Array.empty[Int]
    var required = Map[Int, Int]()

    for( (num, index) <- nums.zipWithIndex) {
 
        var required_num = target - num
        if required.contains(required_num) && response.isEmpty then
            response = Array[Int](required.getOrElse(required_num, -1), index)
 
        required = required + (num -> index)
    }
    response
  }

}