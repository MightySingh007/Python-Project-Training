import datetime
import time
from playsound import playsound

def set_alarm(alarm_time, sound_file="beep.mp3"):
    print(f"Alarm set for {alarm_time}")
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            print("Wake up!")
            playsound(beep.mp3)
            break
        time.sleep(1)

def main():
    alarm_input = input("Enter alarm time (HH:MM:SS): ")
    sound_file = input("Enter sound file path (e.g. ./beep.mp3): ").strip()
    set_alarm(alarm_input, sound_file)

if __name__ == "__main__":
    main()
