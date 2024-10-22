import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

# Authentication - Replace with your credentials
CLIENT_ID = 'your_spotify_client_id'
CLIENT_SECRET = 'your_spotify_client_secret'

# Connect to Spotify API
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Dictionary to map emotions to musical characteristics
emotion_to_genre = {
    'happy': ['pop', 'dance', 'indie'],
    'sad': ['acoustic', 'blues', 'piano'],
    'angry': ['metal', 'rock', 'punk'],
    'relaxed': ['ambient', 'chill', 'classical'],
    'energetic': ['electronic', 'hip-hop', 'funk'],
    'anxious': ['ambient', 'classical', 'jazz'],
    'cheerful': ['pop', 'indie', 'reggae'],
    'stressed': ['jazz', 'chill', 'lo-fi'],
    'dreamy': ['dream-pop', 'ambient', 'shoegaze'],
    'excited': ['dance', 'electronic', 'pop'],
    'bored': ['alternative', 'indie', 'chill'],
    'nostalgic': ['classic rock', 'folk', 'retro'],
    'hopeful': ['pop', 'inspirational', 'uplifting'],
    'content': ['soft rock', 'acoustic', 'country'],
    'romantic': ['pop', 'r&b', 'soul'],
}

# Function to recommend tracks based on emotion
def recommend_tracks(emotion):
    genres = emotion_to_genre.get(emotion.lower(), ['pop'])  # Default to 'pop' if emotion is not found
    selected_genre = random.choice(genres)

    # Fetch recommendations from Spotify
    results = sp.recommendations(seed_genres=[selected_genre], limit=10)  # Increase limit for more results
    tracks = results['tracks']
    
    playlist = []
    for track in tracks:
        track_info = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'url': track['external_urls']['spotify']
        }
        playlist.append(track_info)
    
    return playlist, genres

# Function to get maximum length of strings in a list of dictionaries
def get_max_lengths(playlist):
    max_name_length = max(len(song['name']) for song in playlist) if playlist else 0
    max_artist_length = max(len(song['artist']) for song in playlist) if playlist else 0
    max_url_length = max(len(song['url']) for song in playlist) if playlist else 0
    return max_name_length, max_artist_length, max_url_length

# Main loop for user input
while True:
    emotion = input("\nEnter your emotion (happy, sad, angry, relaxed, energetic, anxious, cheerful, stressed, dreamy, excited, bored, nostalgic, hopeful, content, romantic) or type 'exit' to quit: ").strip().lower()
    
    if emotion == 'exit':
        print("Goodbye my Love!!!")
        break

    # Get playlist based on the emotion
    playlist, genres = recommend_tracks(emotion)

    # Get maximum lengths for formatting
    max_name_length, max_artist_length, max_url_length = get_max_lengths(playlist)

    # Set a minimum width for columns to ensure proper alignment
    min_name_length = max(20, max_name_length)
    min_artist_length = max(15, max_artist_length)
    min_url_length = 35  # Fixed width for URL

    # Display the recommended playlist
    if emotion not in emotion_to_genre:
        print("The emotion you entered is NOT in the list, so we will show you pop music instead.")
    
    print(f"Here are some songs for your '{emotion}' mood:" if emotion in emotion_to_genre else "Here are some pop songs for you:")
    print(f"STT | Song Name{' ' * (min_name_length - 9)} | Artist{' ' * (min_artist_length - 6)} | URL")
    print("-" * (11 + max_name_length + max_artist_length + max_url_length))
    
    for idx, song in enumerate(playlist, 1):
        print(f"{idx:<3} | {song['name']:<{min_name_length}} | {song['artist']:<{min_artist_length}} | {song['url']}")
