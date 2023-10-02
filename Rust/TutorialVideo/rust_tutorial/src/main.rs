//#![allow(unused)]

use rand::Rng;
use std::cmp::Ordering;
use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader, ErrorKind, Write};

fn main() {
    println!("What is your name?");

    let mut name = String::new();
    let greeting = "Nice to meet you";
    io::stdin()
        .read_line(&mut name)
        .expect("Didn't Receive Input");

    println!("Hello {}!, {}!\n\n", name.trim_end(), greeting);

    const ONE_MIL: u32 = 1_000_000;
    const PI: f32 = 3.141592;
    let age = "47";
    let mut age: u32 = age.trim().parse().expect("Age was not assigned a number");

    age += 1;

    println!("I'm {} and I want ${}.\n\n", age, ONE_MIL);

    println!("Max u32: {}.\n", u32::MAX);
    println!("Max u64: {}.\n", u64::MAX);
    println!("Max usize: {}.\n", usize::MAX);
    println!("Max u128: {}.\n", u128::MAX);
    println!("Max f32: {}.\n", f32::MAX);
    println!("Max f64: {}.\n\n", f64::MAX);

    let is_true = true;
    let my_grade = 'A';

    let num_1: f32 = 1.111111111111111;
    println!("f32 : {}.\n", num_1 + 0.111111111111111);
    let num_2: f64 = 1.111111111111111;
    println!("f64 : {}.\n", num_2 + 0.111111111111111);
    let mut num_3: u32 = 5;
    println!("f32 : {}", num_1 + 0.111111111111111);
    let num_4: u32 = 4;
    println!("5 + 4 = {}", num_3 + num_4);
    println!("5 - 4 = {}", num_3 - num_4);
    println!("5 * 4 = {}", num_3 * num_4);
    println!("5 / 4 = {}", num_3 / num_4);
    println!("5 % 4 = {}\n\n", num_3 % num_4);
    num_3 += 1;

    let random_num = rand::thread_rng().gen_range(1..101);
    print!("Random: {}.\n\n", random_num);

    println!("What is your age?");
    let mut my_age = String::new();
    io::stdin()
        .read_line(&mut my_age)
        .expect("Didn't Receive Input");
    let my_age: u32 = my_age
        .trim()
        .parse()
        .expect("Could not convert from String to u32.");

    let can_vote = if my_age >= 18 { true } else { false };

    if (my_age >= 1) && (my_age <= 18) {
        println!("Important Birthday");
    } else if (my_age == 21) || (my_age == 50) {
        println!("Important Birthday");
    } else if (my_age >= 65) {
        println!("Important Birthday");
    } else {
        println!("Not An Important Birthday");
    }
    println!("Can Vote: {}", can_vote);
    println!("\n\n");

    println!("What is your age?");
    let mut my_age2 = String::new();
    io::stdin()
        .read_line(&mut my_age2)
        .expect("Didn't Receive Input");
    let my_age2: u32 = my_age2
        .trim()
        .parse()
        .expect("Could not convert from String to u32.");
    let can_vote2 = if my_age2 >= 18 { true } else { false };

    match my_age2 {
        1..=18 => println!("Important Birthday"),
        21 | 50 => println!("Important Birthday"),
        65..=u32::MAX => println!("Important Birthday"),
        _ => println!("Not An Important Birthday"),
    };
    println!("Can Vote: {}", can_vote2);
    println!("\n\n");

    let my_age3 = 18;
    let voting_age = 18;

    println!("This example age is: {}", my_age3);

    match my_age3.cmp(&voting_age) {
        Ordering::Less => println!("Can't Vote"),
        Ordering::Greater => println!("Can Vote"),
        Ordering::Equal => println!("You just gained the right to vote!"),
    };

    println!("\n\n");

    let arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    println!("1st Index Value: {}", arr_1[0]);
    println!("Length of arr_1: {}", arr_1.len());

    let mut loop_idx = 0;
    loop {
        if arr_1[loop_idx] % 2 != 0 {
            println!("Value: {}", arr_1[loop_idx]);
        }
        loop_idx += 1;
    }
}
