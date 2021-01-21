impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut vec: Vec<i32> = Vec::new();
        for i in 0..nums.len() {
            for j in i+1..nums.len() {
                if(nums[i] + nums[j] == target){
                  vec.push(i as i32);
                  vec.push(j as i32);
                  return vec;
                }
            }   
        }
        return vec;
    }
}