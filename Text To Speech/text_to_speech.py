from gtts import gTTS
import os


def text_to_speech(
    text,
    lang="en",
    tld="com",
    slow=False,
    lang_check=True,
    pre_processor_funcs=None,
    tokenizer_func=None,
    timeout=None,
    output_file="output.mp3",
):
    """
    Convert the provided text to speech and save it as an audio file.

    Args:
        text (string): The text to be read.
        lang (string, optional): The language (IETF language tag) to read the text in. Default is 'en'.
        tld (string, optional): Top-level domain for Google Translate host (e.g., 'com', 'co.uk').
                                This affects accent localization. Default is 'com'.
        slow (bool, optional): If True, reads the text more slowly. Default is False.
        lang_check (bool, optional): If True, enforces valid language, raising a ValueError if unsupported. Default is True.
        pre_processor_funcs (list, optional): List of pre-processing functions to modify the text before tokenizing.
                                                Defaults to a list of built-in pre-processors.
        tokenizer_func (callable, optional): Function to tokenize the text. Defaults to a built-in tokenizer.
        timeout (float or tuple, optional): Seconds to wait for server response. Can be a float or a (connect, read) tuple.
                                            Default is None (wait indefinitely).
        output_file (string): Path for the output audio file (default: 'output.mp3').

    Raises:
        AssertionError: When text is None or empty.
        ValueError: When lang_check is True and lang is unsupported.
    """

    # Use default pre-processor functions if not provided
    if pre_processor_funcs is None:
        pre_processor_funcs = [
            # Example built-in functions from gTTS:
            # Converts tone marks, abbreviations, and deals with word substitutions
            lambda text: text.replace(
                ".", ""
            ),  # You can define more or use built-ins from gTTS
        ]

    # Use default tokenizer if not provided
    if tokenizer_func is None:
        tokenizer_func = lambda text: text.split()  # Basic tokenizer example

    try:
        # Create the gTTS object with the provided arguments
        tts = gTTS(
            text=text,
            lang=lang,
            tld=tld,
            slow=slow,
            lang_check=lang_check,
            pre_processor_funcs=pre_processor_funcs,
            tokenizer_func=tokenizer_func,
            timeout=timeout,
        )

        # Save the audio file
        tts.save("Text To Speech/"+output_file)
        print(f"Audio saved at Text To Speech/{output_file}")

        # Optionally, play the audio file (Windows or Linux/MacOS)
        # if os.name == "nt":  # Windows
        #     os.system(f"start {output_file}")
        # else:  # macOS/Linux
        #     os.system(f"xdg-open {output_file}")

    except AssertionError as ae:
        print(f"Assertion Error: {ae}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")


if __name__ == "__main__":
    # Example usage of the text_to_speech function with various arguments

    # Basic example (English, default options)
    text = "Hello, welcome to the gTTS Python tutorial."
    text_to_speech(text)

    # # Custom example (Spanish, slow speech, and custom file name)
    # text_to_speech(
    #     "Hola, bienvenido al tutorial de gTTS.",
    #     lang="es",
    #     slow=True,
    #     output_file="spanish_slow.mp3",
    # )

    # # Custom example with localized accent (UK English)
    # text_to_speech(
    #     "Hello! How are you today?",
    #     lang="en",
    #     tld="co.uk",
    #     output_file="british_accent.mp3",
    # )

    # # You can pass custom pre-processor functions to modify the text before it’s tokenized.
    # text_to_speech(
    #     "Dr. Smith is a great person.",
    #     pre_processor_funcs=[lambda x: x.replace(".", "")],
    #     output_file="custom_pre-processor.mp3",
    # )

    # # You can set a timeout to limit how long the request to Google Translate waits.
    # text_to_speech(
    #     "This will timeout after 5 seconds.",
    #     output_file="timeout.mp3",
    #     timeout=5.0
    # )
