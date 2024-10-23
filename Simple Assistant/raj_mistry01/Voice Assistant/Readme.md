# Jarvis - A Personal Voice Assistant 🗣️💻

This **Jarvis Personal Assistant** is a Python-based virtual assistant that can execute commands, automate tasks, and provide information at your request. It can help you manage files, open applications, search Wikipedia, forecast weather, and much more—all through voice commands.

## 🚀 Features

1. **Voice & Text Interaction**  
   - Provides **voice recognition** using Google Speech Recognition API.
   - Users can **switch to text mode** if speech recognition fails.
   
2. **Application Management**  
   - Open or close **Notepad** and **Command Prompt**.
   - Manage system **battery levels** with alerts and suggestions.

3. **Information Retrieval**  
   - Get **Wikipedia summaries** for any topic.
   - **Weather forecasts** by city or location-based.
   - Check your **IP address** using an online API.

4. **Entertainment & Media**  
   - Search for **movie details** via IMDb, including cast, plot, and ratings.
   - Open **YouTube** and automate subscriptions.

5. **System Control**  
   - Adjust **volume controls**: Increase, decrease, or mute.
   - Minimize or maximize windows using **keyboard automation**.
   - Track **internet speed** with Speedtest integration.

6. **Utility Features**  
   - Control **Webcam** access and capture videos.
   - Perform calculations using **Wolfram Alpha**.
   - Automatically **open websites** using Chrome.
   - Monitor **system processes** and terminate them on command.

---

## 🔧 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/jarvis-assistant.git
   cd jarvis-assistant
   ```

2. **Install Dependencies**  
   Install all necessary Python packages using:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add Paths for Applications**
   Set the paths for:
   - **Chrome browser**: `"C:/Program Files/Google/Chrome/Application/chrome.exe"`
   - **Notepad**: `"C:/Windows/System32/notepad.exe"`
   - **Visual Studio Code** (optional): Adjust the path as per your installation.

4. **Get API Keys**
   - **OpenWeather API**: [Sign up here](https://openweathermap.org/) and replace `apiKey` in the code.
   - **Wolfram Alpha API**: Get an API key [here](https://products.wolframalpha.com/api/).

---

## 🧑‍💻 Usage Instructions

1. **Launch the Assistant**  
   Run the script:
   ```bash
   python jarvis.py
   ```

2. **Speak Commands**:
   - "Open Notepad" – Launches Notepad.
   - "What is the weather report?" – Gives the weather of your current location.
   - "Search for Titanic on Wikipedia" – Provides a brief Wikipedia summary.
   - "Close Command Prompt" – Terminates the Command Prompt if running.
   - "What's my IP address?" – Provides your public IP address.

3. **Text Mode**  
   If the voice input isn't recognized, type your queries when prompted.

4. **Pause or Stop Listening**:
   - Say **"Stop listening"**: Pauses the assistant.
   - Resume by pressing **Ctrl + Alt + K**.
   - Say **"No query, thanks"** to exit the assistant.

---

## 🌦️ Example Queries

- **"How are you, Jarvis?"**  
  → Jarvis responds and continues the conversation.

- **"Open Command Prompt"**  
  → Opens the Command Prompt window.

- **"Mute the volume"**  
  → Mutes system volume.

---

## 🎯 Known Issues and Limitations

- Some queries require accurate phrasing.
- Voice recognition may fail in noisy environments.
- Web automation depends on having Chrome installed.
- Weather reports return temperature in **Kelvin** by default (can be adjusted).

---

## 💡 Future Improvements

- Add **Gmail** integration to send emails.
- Support for **natural conversations** with chat history.
- **Alarm feature** implementation.

---

## 🤖 Contribution

Feel free to submit pull requests or report bugs/issues. Contributions are welcome to make this assistant smarter and more responsive!

---


## 🛠️ Prerequisites

- **Python 3.7+**
- Required Packages (install via `pip`):
  ```bash
  pip install -r requirements.txt

---
## 🛠️ Api Credits

    Wolfram Api
    OpenWheather Api


- **Python 3.7+**
- Required Packages (install via `pip`):
  ```bash
  pip install -r requirements.txt

Enjoy using **Jarvis Personal Assistant**! 😊
