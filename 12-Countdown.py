import time
def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
try:
    total_time = int(input("Enter countdown time in seconds: "))
    countdown(total_time)
except ValueError:
    print("Please enter a valid number.")
