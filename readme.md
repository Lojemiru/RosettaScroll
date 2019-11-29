# RosettaScroll
Rudimentary auto-translation for the Archivist Alphabet. If you don't know what that means, you need to play The Messenger and join their Discord server.

# Prerequisites
Python 3.X: https://www.python.org/downloads/

Tesseract-OCR: https://github.com/tesseract-ocr/tesseract (platform-dependent, follow normal installation instructions.)

Python packages: pytesseract, pyperclip, Pillow

# Installation
Clone the repository locally.

Install `ArchivistAlphabet.ttf` as you would any other font.

Copy `ArchivistAlphabe.traineddata` (yes, that's how it should be spelled) to your tessdata folder. Mine is under `D:\Program Files\Tesseract-OCR\tessdata`.

Open `RosettaScroll.py` with your favorite text editor and set `pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'` to your `tesseract.exe` installation location. If you installed it for all users, it should be in a very similar location. Save and close `RosettaScroll.py`.

Run the script and enter your filename for image-to-text translation! It will likely need some cleaning up afterwards, but the majority of the characters should be properly translated.
