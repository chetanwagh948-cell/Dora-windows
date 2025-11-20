import time
import pyautogui


def type_in_editor(text: str, delay: float = 0.02):
    """
    After a short delay, type the given text into the active window
    (VS Code, Android Studio, etc).
    """
    # Give you 1 second to click into the editor
    time.sleep(1.0)
    pyautogui.write(text, interval=delay)
