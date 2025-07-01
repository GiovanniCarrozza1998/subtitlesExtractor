# Python Subtitles Extraction Tool
This project is a Python tool for extracting subtitles displayed in a user-selected screen region. The project consists of four main scripts:

regionSelector.py: Contains the RegionSelector class, which uses the tkinter package to allow the user to select the screen area where subtitles are displayed.

subExtractor.py: Contains the main function and defines the program workflow. After the user selects the screen region, a thread is started to capture screenshots at regular intervals. The extraction continues until the user indicates they wish to stop.

textExtractor.py: Provides methods to transform each screenshot by converting pixels that are not sufficiently white to black. This helps tesseract OCR better detect the text present in the screenshots.

textCleaner.py: Uses methods to clean the extracted text by removing strange characters and redundancies through interaction with the gemini-1.5-flash model and to save the cleaned text into the working directory specified in the config.json file.

Installation:

To use the tool you need to clone the repository, install tesseract OCR and provide a valid Google API Key. 

Usage
1) Run the Main Script: python subExtractor.py
2) Select the Region: use the interface to select the screen region containing the subtitles.
3) Extract Subtitles: the program will capture screenshots and extract subtitles until you decide to stop it.
4) Cleaning and saving subtitles: the program joins the collection of texts, clean it and then save it to a .txt file in thw specified working directory.

Requirements: libraries listed in requirements.txt
