import google.generativeai as genai
from datetime import datetime
import json

# Load configurations
with open('config.json') as config_file:
    config = json.load(config_file)

genai.configure(api_key=config["api_key"])
model = genai.GenerativeModel("gemini-1.5-flash")


def clean_text(text_collection):
    """Cleans and reconstructs text using a generative AI model."""
    full_text = '\n'.join(text_collection)
    prompt = f"Ricostruisci il testo riportata nel testo riportato nel seguito. Il testo è stato estratto mediante continui screenshot equidistanziati nel tempo (1 secondo di delay) con l'uso di tesseract OCR. TESTO : {full_text}"

    try:
        response = model.generate_content(prompt).text
        print(f"OUTPUT GEMINI: {response}")
    except Exception as e:
        print(f"Error generating content: {e}")
        response = ""

    with open(
            f"{config['screenshots_directory']}\\output_grezzo_" + f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt",
            'w', encoding='utf-8') as f:
        f.write(full_text)
    with open(f"{config['screenshots_directory']}\\output_" + f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt",
              'w', encoding='utf-8') as f:
        f.write(response)