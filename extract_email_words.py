import time
import psutil

def extract_words_from_email(email):
    if "@" in email:
        username = email.split("@")[0]
        words = username.split(".")
        return words
    else:
        return []

if __name__ == "__main__":
    email = "example.user@gmail.com"  # Replace with the email address you want to extract from
    start_time = time.time()

    words = extract_words_from_email(email)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Words before @:", words)
    print("Execution Time: {:.6f} seconds".format(execution_time))

    # Measure resource usage
    process = psutil.Process()
    memory_info = process.memory_info()
    cpu_percent = psutil.cpu_percent(interval=1)

    print("Memory Usage: {} bytes".format(memory_info.rss))
    print("CPU Usage: {:.2f}%".format(cpu_percent))
