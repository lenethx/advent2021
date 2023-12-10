use std::io::{self, BufReader};
use std::io::prelude::*;
use std::fs::File;
use std::collections::HashMap;

fn main() -> std::io::Result<()>{
    let f = File::open("input.txt")?;
    let f = BufReader::new(f);

    let mut sumscore = 0;
    let vals = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let lines = f.lines().map(|istr| {istr.unwrap().as_bytes()}).map(|jstr| { [&jstr[0..jstr.len()/2],&jstr[jstr.len()/2..]]  } );
    let lines = lines.map(|istr| { istr.map( |jstr| {println!("{:?}", jstr)} ) });
    //println!("{}", lines.map(|istr| { (istr[0] & istr[1]).log2() }).sum());
/*
    for line in f.lines() {
        sumscore += possiblescores.get(&line.unwrap() as &str).unwrap(); 
    }
  */  
    Ok(())
}
