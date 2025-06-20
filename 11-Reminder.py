import time

def set_reminder():
    message = input("What should I remind you about? ")
    delay = int(input("In how many seconds should I remind you? "))

    print(f"Reminder set! I will remind you in {delay} seconds.")
    time.sleep(delay)
    print(f"\n⏰ Reminder: {message}")

# Run the reminder
set_reminder()
