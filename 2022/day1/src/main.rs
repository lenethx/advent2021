use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;

fn main() -> std::io::Result<()>{
    let f = File::open("input.txt")?;
    let f = BufReader::new(f);

    let mut highest = [0,0,0];
    let mut current = 0u64;

 
    for line in f.lines() {
        let line = line.unwrap();
        if line == "" {
            for item in highest.iter_mut() {
                if current > *item {
                    *item = current; 
                    break;
                }
            }
            highest.sort();
           current = 0;
        } else {
            current += line.parse::<u64>().unwrap();
        }
    }
    
    println!("{}", highest.iter().sum::<u64>());
    println!("{:?}", highest);
    Ok(())
}
