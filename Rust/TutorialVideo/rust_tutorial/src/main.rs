//#![allow(unused)]

use rand::Rng;
use std::cmp::Ordering;
use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader, ErrorKind, Write};

fn main() {
    say_hello();
    get_sum(5, 4);
    println!("{}", get_sum2(2, 2));
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

    let arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
    println!("1st Index Value: {}", arr_1[0]);
    println!("Length of arr_1: {}", arr_1.len());

    let mut loop_idx = 0;

    loop {
        if arr_1[loop_idx] % 2 == 0 {
            println!("Value: {}", arr_1[loop_idx]);
            loop_idx += 1;
            continue;
        }
        if arr_1[loop_idx] == 9 {
            println!("Limit reached.");
            break;
        }
        loop_idx += 1;
    }

    while loop_idx < arr_1.len() {
        println!("Arr: {}", arr_1[loop_idx]);
        loop_idx += 1;
    }

    for val in arr_1.iter() {
        println!("Val: {}", val);
    }

    let my_tuple: (u8, String, f64) = (47, "Derek".to_string(), 50_000.0);

    println!("Name: {}", my_tuple.1);

    let (v1, v2, v3) = my_tuple;
    println!("Age: {}", v1);

    let mut st1 = String::new();
    st1.push('A');
    st1.push_str("word");

    for word in st1.split_whitespace() {
        println!("{}", word);
    }

    let st2 = st1.replace("A", "Another");
    println!("{}", st2);

    let st3 = String::from(" x r t b h k k a m c");

    let mut v4: Vec<char> = st3.chars().collect();
    v4.sort();
    v4.dedup();

    for char in v4 {
        println!("{}", char);
    }

    let st4: &str = "Random String";
    let mut st5 = st4.to_string();
    println!("{}", st5);

    let byte_arr1 = st5.as_bytes();

    let st6 = &st5[0..6];

    println!("String length: {}", st6.len());

    st5.clear();

    let st6 = String::from("Just some");
    let st7 = String::from(" words");
    let st8 = st6 + &st7;

    for char in st8.bytes() {
        println!("{}", char);
    }

    let int_u8: u8 = 5;
    let int2_u8: u8 = 4;

    let in3_u32: u32 = (int_u8 as u32) + (int2_u8 as u32);

    enum Day {
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
        Sunday,
    }

    impl Day {
        fn is_weekend(&self) -> bool {
            match self {
                Day::Saturday | Day::Sunday => true,
                _ => false,
            }
        }
    }

    let today: Day = Day::Monday;
    let today0: Day = Day::Saturday;
    let today1: Day = Day::Sunday;

    match today {
        Day::Monday => println!("Everyone hates Monday"),
        Day::Tuesday => println!("Donut day"),
        Day::Wednesday => println!("Hump day"),
        Day::Thursday => println!("Pay day"),
        Day::Friday => println!("Almost Weekend"),
        Day::Saturday => println!("Weekend"),
        Day::Sunday => println!("Weekend"),
    }
    println!("Is today the weekend? {}", today.is_weekend());
    println!("Is today the weekend? {}", today0.is_weekend());
    println!("Is today the weekend? {}", today1.is_weekend());

    let vec1: Vec<i32> = Vec::new();
    let mut vec2 = vec![1, 2, 3, 4];
    vec2.push(5);
    println!("1st: {}", vec2[0]);

    let second: &i32 = &vec2[1];

    match vec2.get(1) {
        Some(second) => println!("2nd: {}", second),
        None => println!("No 2nd value"),
    }

    for i in &mut vec2 {
        *i *= 2;
    }

    for i in &vec2 {
        println!("{}", i);
    }
    println!("Vec Length: {}", vec2.len());
    println!("Pop: {:?}", vec2.pop());

    fn say_hello() {
        println!("Hello");
    }

    fn get_sum(x: i32, y: i32) {
        println!("{} + {} = {}", x, y, x + y);
    }
    fn get_sum2(x: i32, y: i32) -> i32 {
        return x + y;
    }
    fn get_2(x: i32) -> (i32, i32) {
        return (x + 1, x + 2);
    }

    fn sum_list(list: &[i32]) -> i32 {
        let mut sum = 0;
        for &val in list.iter() {
            sum += &val;
        }
        sum
    }

    let (val1, val2) = get_2(1);
    println!("Val1: {} , Val2: {}", val1, val2);

    let num_list = vec![1, 2, 3, 4, 5];

    println!("Sum of list = {}", sum_list(&num_list));
}
