impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle == "" {
            return 0;
        }
        let result = haystack.find(&needle);

        match result {
            Some(x) => {return x as i32 },
            None => {return -1}
        }
    }
}