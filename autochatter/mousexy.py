import pyautogui
import time

print("Move your mouse to the desired location within 5 seconds...")
time.sleep(5)  # Gives you time to move your mouse

# Prints the current mouse position
current_mouse_x, current_mouse_y = pyautogui.position()
print(f"Current mouse position: X={current_mouse_x}, Y={current_mouse_y}")
