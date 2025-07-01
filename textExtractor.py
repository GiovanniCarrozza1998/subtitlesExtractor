from PIL import Image
import pytesseract
import json

# Load configurations
with open('config.json') as config_file:
    config = json.load(config_file)

pytesseract.pytesseract.tesseract_cmd = config["tesseract_path"]

def binarizza_img_non_bianca_in_nero(percorso_immagine, percorso_output):
    """Convert a non-white image to binary (black and white)."""
    try:
        img = Image.open(percorso_immagine).convert('RGB')
        dati = img.load()
        larghezza, altezza = img.size

        for x in range(larghezza):
            for y in range(altezza):
                r, g, b = dati[x, y]
                dati[x, y] = (255, 255, 255) if (r>=220 and g>=220 and b>=220) else (0, 0, 0)

        img.save(percorso_output)
    except Exception as e:
        print(f"Error processing image: {e}")
    finally:
        img.close()

def estrai_testo_immagine(percorso_immagine, language):
    """Extracts text from an image using OCR."""
    try:
        immagine = Image.open(percorso_immagine)
        testo = pytesseract.image_to_string(immagine, lang=language)
        return testo
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""