# Auto-translation for ARG scrolls. Should work for most things written in the Archivist font.
import pytesseract, time, pyperclip
try:
    from PIL import Image
except:
    import Image

# Input shenanigans. Makes this look cooler than it really is.
print("Enter filename to ", end="", flush=True)
time.sleep(.8)
print("DO ", end="", flush=True)
time.sleep(.5)
print("THE ", end="", flush=True)
time.sleep(.5)
print("THING", end="", flush=True)
time.sleep(.5)
print("!", end="", flush=True)
time.sleep(.1)
print("!", end="", flush=True)
time.sleep(.1)
file = input("!\n")

# Set Tesseract EXE install location
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

# Translation, for whatever reason my font was misnamed.
def translate_core(filename):
    text = pytesseract.image_to_string(Image.open(filename), lang="ArchivistAlphabe")
    return text

# Translate image and store it as a string
string = translate_core(file)

# Translation output
print("\n\n\n"+string)

# Copy translation to clipboard
pyperclip.copy(string)


time.sleep(.2)
print("\n[Translation copied to clipboard]")

time.sleep(15)
