impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let reversed: String = x.to_string().chars().rev().collect();
        x.to_string() ==  reversed
    }
}