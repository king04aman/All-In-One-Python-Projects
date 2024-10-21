import pytesseract
from PIL import Image
import os

def extract_text_from_image(image_path):
    """Extracts text from an image file using Tesseract OCR."""
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use pytesseract to do OCR on the image
            extracted_text = pytesseract.image_to_string(img)
            return extracted_text
    except Exception as e:
        print(f"Error processing the image: {e}")
        return None

def main():

    image_path = input("Enter the path to the image file: ")

    if not os.path.isfile(image_path):
        print("File does not exist. Please check the path and try again.")
        return
    text = extract_text_from_image(image_path)

    if text:
        print("Extracted Text:")
        print(text)

if __name__ == "__main__":
    main()
