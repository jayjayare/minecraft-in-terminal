import os
import time
import mss
from PIL import Image

def main():
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    target_height = 160  # Number of lines (rows)

    with mss.mss() as sct:
        monitor = sct.monitors[1]  # monitor to be recorded to terminal

        while True:
            # Capture screen from primary monitor
            screenshot = sct.grab(monitor)
            img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)

            # Resize image for ASCII output
            width, height = img.size
            aspect_ratio = height / width / 2
            target_width = int(target_height / aspect_ratio)
            gray_img = img.resize((target_width, target_height)).convert("L")
            pixels = gray_img.getdata()

            # Convert pixels to ASCII characters
            ascii_str = "".join([ascii_chars[pixel // 25] for pixel in pixels])
            lines = [ascii_str[i:i + target_width] for i in range(0, len(ascii_str), target_width)]

            # Output to terminal
            os.system("clear")
            print("\n".join(lines))

            time.sleep(0.1)

