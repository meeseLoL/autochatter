import pyautogui
import random
import time

# Step 1: Define the boundaries for the chat box
min_x, max_x = min(-570, -573, -1040, -1040), max(-570, -573, -1040, -1040)
min_y, max_y = min(-1639, -1540, -1544, -1638), max(-1639, -1540, -1544, -1638)

# Step 2: Function to generate a random point within the rectangle
def random_point_within_bounds():
    x = random.randint(min_x, max_x)
    y = random.randint(min_y, max_y)
    return x, y

# Step 3: Function to load a random text line from the file
def load_random_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return random.choice(lines).strip()

# Step 4: Function to type text with a delay between keystrokes
def type_text(text, min_delay=0.05, max_delay=0.15):
    for char in text:
        pyautogui.write(char, interval=random.uniform(min_delay, max_delay))
    pyautogui.press('enter')  # Press Enter after typing the text

# Step 5: Function to click within the bounds, type the random text, and hit enter
def type_random_message(file_path):
    # Click at a random point within bounds
    x, y = random_point_within_bounds()
    pyautogui.click(x, y)
    print(f"Clicked at X={x}, Y={y}")

    # Load random text from the file
    random_text = load_random_text(file_path)
    
    # Type the random text and hit enter with delays
    type_text(random_text)
    print(f"Typed and sent: {random_text}")

# Step 6: Main loop to run the program at random intervals
if __name__ == "__main__":
    file_path = "random.txt"  # Path to your text file

    try:
        while True:
            type_random_message(file_path)
            
            # Random sleep time between 2 to 17 minutes
            sleep_time = random.randint(120, 1020)
            print(f"Sleeping for {sleep_time // 60} minutes and {sleep_time % 60} seconds...")
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("Program terminated.")
