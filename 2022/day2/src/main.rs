use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;
use std::collections::HashMap;

fn main() -> std::io::Result<()>{
    let f = File::open("input.txt")?;
    let f = BufReader::new(f);

    let mut sumscore = 0;
    let possiblescores = HashMap::from([
        ("A X", 3), //rock scissors
        ("A Y", 4), // rock rock
        ("A Z", 8), //rock paper
        ("B X", 1), //paper rock
        ("B Y", 5), // paper paper
        ("B Z", 9), //paper scissors
        ("C X", 2),
        ("C Y", 6),
        ("C Z", 7)

        ]);
 
    for line in f.lines() {
        sumscore += possiblescores.get(&line.unwrap() as &str).unwrap(); 
    }
    
    println!("{:?}", sumscore);
    Ok(())
}
