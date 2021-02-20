use std::io::{self, BufRead};

fn selection_sort(n:u32, &arr: Vec<i32>) => Vec<i32> {

    
}

fn main() {
    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();
    let n: u32 = iterator.next().unwrap().unwrap().parse().unwrap();
    println!("n is {:#?}", n);
    let input = iterator.next().unwrap().unwrap();
    let arr: Vec<i32> = input.split(' ').into_iter().map(|x| x.parse::<i32>().unwrap()).collect();
    println!("b is {:#?}", &b);

    let sorted_arr = selection_sort(n, arr);

    println!("after sorting: {:#?}", &selection_sort(n, arr))
}