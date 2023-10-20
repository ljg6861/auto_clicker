import pyautogui
import time
import random
import keyboard


def auto_clicker(interval_min=0.71425, interval_max=1.94212, break_interval_min=600, break_interval_max=1020,
                 break_duration_min=60, break_duration_max=180):
    """
    Human-like Autoclicker Function with Pause Feature
    :param interval_min: Minimum time interval between clicks in seconds.
    :param interval_max: Maximum time interval between clicks in seconds.
    :param break_interval_min: Minimum time interval between breaks in seconds.
    :param break_interval_max: Maximum time interval between breaks in seconds.
    :param break_duration_min: Minimum break duration in seconds.
    :param break_duration_max: Maximum break duration in seconds.
    :return: None
    """
    is_paused = False
    next_break = time.time() + random.uniform(break_interval_min, break_interval_max)

    def toggle_pause(e):
        nonlocal is_paused
        is_paused = not is_paused
        status = "paused" if is_paused else "unpaused"
        print(f"Autoclicker has been {status}.")

    keyboard.on_press_key("esc", toggle_pause)

    try:
        while True:
            if is_paused:
                time.sleep(1)
                continue

            if time.time() >= next_break:
                break_duration = random.uniform(break_duration_min, break_duration_max)
                print(f"Taking a break for {break_duration:.2f} seconds.")
                time.sleep(break_duration)
                next_break = time.time() + random.uniform(break_interval_min, break_interval_max)

            pyautogui.click()
            interval = random.uniform(interval_min, interval_max)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Autoclicker stopped.")


if __name__ == "__main__":
    auto_clicker()
