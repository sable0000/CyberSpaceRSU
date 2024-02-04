import os
import time
import requests

# Corrected URLs for raw content (replace these with your actual raw file URLs)
file1_url = "https://raw.githubusercontent.com/sable0000/CyberSpaceRSU/main/ascii-art.txt"
file2_url = "https://raw.githubusercontent.com/sable0000/CyberSpaceRSU/main/ascii-art%20(1).txt"

# Interval in seconds for how long each file is displayed before switching
interval = 1

def clear_screen():
    # Clear the screen. Works on Windows and Unix systems.
    os.system('cls' if os.name == 'nt' else 'clear')

def fetch_and_display(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        print(response.text)
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

while True:
    clear_screen()
    fetch_and_display(file1_url)
    time.sleep(interval)
    clear_screen()
    fetch_and_display(file2_url)
    time.sleep(interval)
