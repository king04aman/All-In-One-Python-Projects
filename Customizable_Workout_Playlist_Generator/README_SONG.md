# Customizable Workout Playlist Generator

This Python application generates customized workout playlists based on user preferences, including workout type, duration, preferred genres, and BPM range. It can use a local song database or integrate with popular music streaming services like Spotify, Apple Music, and YouTube Music.

## Features

- Generate playlists for various workout types (e.g., HIIT, yoga, cardio)
- Customize playlist duration
- Filter songs by genre and BPM range
- Integration with Spotify, Apple Music, and YouTube Music (API keys required)
- Save and load playlists in JSON format

## Requirements

- Python 3.6+
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Ashutoshdas-dev/All-In-One-Python-Projects.git
   cd Customizable_Workout_Playlist_Generator
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up API credentials for the music services you want to use (Spotify, Apple Music, or YouTube Music).

## Usage

1. Run the main script:
   ```
   python playlist.py
   ```

2. Follow the prompts to:
   - Choose a music source (local database, Spotify, Apple Music, or YouTube Music)
   - Enter workout type, duration, preferred genres, and BPM range
   - Generate and view the playlist
   - Save the playlist to a JSON file (optional)

3. Repeat the process to generate multiple playlists or exit the program.

## API Integration

To use the music streaming service integrations, you'll need to set up API credentials:

- Spotify: Set up a Spotify Developer account and create an app to get your client ID and client secret.
- Apple Music: Obtain an Apple Developer account and set up MusicKit.
- YouTube Music: No authentication is required for basic usage.

Update the respective client classes in `playlist.py` with your API credentials.
