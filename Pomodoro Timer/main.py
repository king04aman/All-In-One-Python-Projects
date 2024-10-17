import time


def countdown(minutes, label):
    total_seconds = minutes * 60
    while total_seconds:
        minutes, seconds = divmod(total_seconds, 60)
        timer = f"{minutes:02d}:{seconds:02d}"
        print(f"{label} Timer: {timer}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(f"\n{label} finished!")


def pomodoro_timer(work_min, short_break_min, long_break_min, cycles):
    for i in range(cycles):
        print(f"\nCycle {i+1} of {cycles}")
        countdown(work_min, "Work")
        if i < cycles - 1:
            countdown(short_break_min, "Short Break")
        else:
            countdown(long_break_min, "Long Break")


if __name__ == "__main__":
    work_minutes = int(input("Enter work interval in minutes: "))
    short_break_minutes = int(input("Enter short break interval in minutes: "))
    long_break_minutes = int(input("Enter long break interval in minutes: "))
    cycles = int(input("Enter the number of cycles: "))

    pomodoro_timer(work_minutes, short_break_minutes, long_break_minutes, cycles)
