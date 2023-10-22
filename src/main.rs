use std::time::{Instant};
use psutil::prelude::*;
use psutil::memory::VirtualMemory;
use psutil::cpu::CpuPercentCollector;

fn extract_words_from_email(email: &str) -> Vec<&str> {
    let mut words: Vec<&str> = vec![];

    if let Some(index) = email.find('@') {
        let username = &email[..index];
        words = username.split('.').collect();
    }

    words
}

fn main() {
    let email = "example.user@gmail.com"; // Replace with the email address you want to extract from

    let start_time = Instant::now();
    let words = extract_words_from_email(email);
    let end_time = start_time.elapsed();

    println!("Words before @: {:?}", words);
    println!("Execution Time: {:?}", end_time);

    // Measure resource usage
    let memory = VirtualMemory::new().unwrap();
    let cpu_percent_collector = CpuPercentCollector::new().unwrap();

    println!("Memory Usage: {} bytes", memory.resident());
    println!("CPU Usage: {:.2}% (1-second interval)", cpu_percent_collector.percent().unwrap());
}
