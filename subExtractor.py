from datetime import datetime
import threading
import time
import pyautogui
import regionSelector
import textExtractor
import os
import textCleaner
import json

# Load configurations
with open('config.json') as config_file:
    config = json.load(config_file)

screenshot_directory = config["screenshots_directory"]
running = True
contatore = 0

def clean(contatore):
    """Removes temporary screenshot files."""
    for i in range(contatore):
        try:
            os.remove(f"{screenshot_directory}\\{i}.png")
            os.remove(f"{screenshot_directory}\\{i}_output.png")
        except Exception as e:
            print(f"Error removing file: {e}")

def check_will():
    """Waits for user input to stop the running process."""
    global running
    print("Type anything to terminate the execution!")
    input()
    running = False

def take_screenshot(left, top, right, bottom):
    """Continuously takes screenshots of a defined region until stopped."""
    global running, contatore, language

    while running:
        try:
            screenshot_region(left, top, right, bottom, f"{screenshot_directory}\\{contatore}.png")
            contatore += 1
            time.sleep(1)
        except Exception as e:
            print(f"Error taking screenshot: {e}")
            running = False

    print("Screenshot capture ended. Proceeding to text extraction.")
    text_collection = []
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    for i in range(contatore):
        try:
            textExtractor.binarizza_img_non_bianca_in_nero(
                f"{screenshot_directory}\\{i}.png",
                f"{screenshot_directory}\\{i}_output.png"
            )
            text_collection.append(
                f"Ora testo registrato {datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}: " +
                textExtractor.estrai_testo_immagine(f"{screenshot_directory}\\{i}_output.png", config["language"])
            )
        except Exception as e:
            print(f"Error extracting text: {e}")

    textCleaner.clean_text(text_collection)
    print("Execution is terminating.")
    clean(contatore)

def salva_lista_su_file(lista_stringhe, percorso_file):
    """Saves a list of strings to a file."""
    with open(percorso_file, 'w', encoding='utf-8') as f:
        for riga in lista_stringhe:
            f.write(riga + '\n')

def screenshot_region(left, top, right, bottom, output_path):
    """Captures a screenshot of the specified region."""
    width = right - left
    height = bottom - top
    region = (left, top, width, height)
    img = pyautogui.screenshot(region=region)
    img.save(output_path)

if __name__ == "__main__":
    selector = regionSelector.RegionSelector()
    selector.mainloop()
    left, right, top, bottom = selector.get_region()
    screenshot_thread = threading.Thread(target=take_screenshot, args=(left, top, right, bottom))
    screenshot_thread.start()
    input_thread = threading.Thread(target=check_will)
    input_thread.start()