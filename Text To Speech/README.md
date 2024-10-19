# Script Name
**Text to Speech Converter using gTTS**

- This script converts text into speech using Google’s Text-to-Speech (gTTS) API and saves the output as an audio file (e.g., `.mp3` format).
- It allows for customization of language, speech speed, accents, and other pre-processing and tokenizing options.
- Features:
  - Support for multiple languages using IETF language tags.
  - Localized accents via different Google Translate top-level domains (`tld`).
  - Option to slow down speech for easier comprehension.
  - Custom text pre-processing and tokenization options.
  - Timeout control for network requests.
  - Automatic playing of the audio file after saving (optional).

# Description
This script provides a convenient interface for converting text into speech using the `gTTS` library. The text can be read in multiple languages, at different speeds, and with various localized accents. The script also includes advanced options for pre-processing the input text and customizing how it's tokenized before being sent to the gTTS API.

### Key Features:
- **Multilingual Support**: Specify different languages using IETF language tags (`en`, `es`, etc.).
- **Accents**: Use top-level domains (`tld`), such as `com`, `co.uk`, etc., to localize the accent.
- **Custom Speed**: Option to slow down the speech for better understanding.
- **Pre-Processing**: Built-in support for text pre-processing (e.g., removing punctuation).
- **Timeout**: Set timeout limits for the API request.

# Prerequisites
The following libraries are required to run the script:
```bash
pip install gtts
```

Additionally, the script uses built-in libraries like `os`.

# Installing Instructions
1. **Clone the Repository**:
   Clone this repository to your local machine using:
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies**:
   Navigate to the project directory and install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**:
   After cloning and installing dependencies, you can run the script directly:
   ```bash
   python text_to_speech.py
   ```

4. **Customize the Script**:
   You can modify the input text, language, speed, and other options directly in the script:
   ```python
   text_to_speech("Hello, welcome to the gTTS Python tutorial.", lang='en', slow=False)
   ```

# Output
### Example output:
After running the script with the text `"Hello, welcome to the gTTS Python tutorial."`, the output file `output.mp3` is generated.


# Author
**[Himanshu Mahajan](https://github.com/himanshumahajan138)**
