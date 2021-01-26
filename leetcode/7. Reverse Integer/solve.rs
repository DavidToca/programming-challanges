
impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let a: String = x.to_string();
        let sign: char = a.chars().nth(0).unwrap();
        
        if sign == '-' {
            a = a[1..a.chars().count()-1];
        }
        // reverse
        a = a.graphemes(true).rev().collect();
        // add sign to a
        if sign == '-' {
            a = a.to_owned();
            a = a + sign;
        }
        return a;
    }
}

