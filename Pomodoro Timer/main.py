import time


def countdown(minutes, label):
    total_seconds = minutes * 60
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"{label} Timer: {timer}", end="\r")
        time.sleep(1)
        total_seconds -= 1
    print(f"\n{label} finished!")


def handle_pause_stop():
    while True:
        user_input = input(
            "\nPress 'p' to pause, 's' to stop, or 'Enter' to continue: "
        ).lower()
        if user_input == "p":
            print("Timer paused. Press 'Enter' to resume.")
            input()
        elif user_input == "s":
            print("Timer stopped.")
            return True  # Return True to signal that the timer should stop
        else:
            return False  # Return False to continue with the timer


def pomodoro_timer(work_min, short_break_min, long_break_min, cycles):
    for i in range(cycles):
        print(f"\nCycle {i+1} of {cycles}")
        countdown(work_min, "Work")
        if i < cycles - 1:
            print("\nStarting short break...")
            if handle_pause_stop():
                return
            countdown(short_break_min, "Short Break")
        else:
            print("\nStarting long break...")
            if handle_pause_stop():
                return
            countdown(long_break_min, "Long Break")
            if not repeat_or_end():
                return


def repeat_or_end():
    user_input = input(
        "\nCycle finished. Would you like to repeat the cycle? (y/n): "
    ).lower()
    return user_input == "y"


def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    work_minutes = get_valid_input("Enter work interval in minutes: ")
    short_break_minutes = get_valid_input("Enter short break interval in minutes: ")
    long_break_minutes = get_valid_input("Enter long break interval in minutes: ")
    cycles = get_valid_input("Enter the number of cycles: ")

    pomodoro_timer(work_minutes, short_break_minutes, long_break_minutes, cycles)
