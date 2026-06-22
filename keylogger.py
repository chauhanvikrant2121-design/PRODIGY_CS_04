from pynput.keyboard import Key, Listener

# The text file where your recorded typing will be saved
log_file = "key_log.txt"

def on_press(key):
    with open(log_file, "a", encoding="utf-8") as f:
        try:
            # Save normal letters and numbers
            f.write(key.char)
        except AttributeError:
            # Save spaces and new lines cleanly; skip other system keys
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")

def on_release(key):
    # Stop the program when you press the ESC key
    if key == Key.esc:
        return False

# Start the background listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()