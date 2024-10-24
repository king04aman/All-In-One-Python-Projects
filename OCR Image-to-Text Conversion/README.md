## Introduction

Image Text Extractor is a Python application that utilizes Tesseract OCR to extract text from images. This application allows users to input the path to an image file and receive the extracted text in return.

## Requirements

- Python 3.x
- Libraries:
  - `pytesseract`
  - `PIL` (Pillow)

You can install the required libraries by running:

```bash
    pip install pytesseract Pillow
```

## Installation Instructions for All Operating Systems

### Windows

1. **Install Python**:

   - Download and install Python from the [official website](https://www.python.org/downloads/).
   - During installation, make sure to check the box that says "Add Python to PATH".

2. **Install Tesseract OCR**:

   - Download the Tesseract installer from the [Tesseract GitHub releases page](https://github.com/tesseract-ocr/tesseract/releases).
   - Run the installer and note the installation path (usually `C:\Program Files\Tesseract-OCR`).

3. **Set Tesseract Path**:

   - Add the Tesseract installation path to your system environment variables.
     - Right-click on "This PC" or "My Computer" > Properties > Advanced system settings > Environment Variables.
     - Under "System variables", find the `Path` variable and click Edit. Add the Tesseract path.

4. **Install Required Libraries**:
   - Open Command Prompt and run:
     ```bash
     pip install pytesseract Pillow
     ```

### macOS

1. **Install Homebrew** (if not already installed):

   - Open Terminal and run:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

2. **Install Python**:

   - Use Homebrew to install Python:
     ```bash
     brew install python
     ```

3. **Install Tesseract OCR**:

   - Install Tesseract using Homebrew:
     ```bash
     brew install tesseract
     ```

4. **Install Required Libraries**:
   - In Terminal, run:
     ```bash
     pip install pytesseract Pillow
     ```

### Linux (Ubuntu/Debian)

1. **Install Python** (if not already installed):

   - Open Terminal and run:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Install Tesseract OCR**:

   - Install Tesseract using:
     ```bash
     sudo apt install tesseract-ocr
     ```

3. **Install Required Libraries**:
   - In Terminal, run:
     ```bash
     pip3 install pytesseract Pillow
     ```

## Usage Instructions

After completing the installation, follow the usage instructions below to run the application.

1. Open Command Prompt.
2. Navigate to the directory where the script is located using the `cd` command:
   ```bash
    cd path\to\your\script
   ```
3. Run the Python script
   ```bash
    python image_text_extractor.py - mine is main.py
   ```