import json
from datetime import timedelta
import random
from typing import List, Dict, Optional
import os

# Add these imports for API integration (you'll need to install these libraries)
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from ytmusicapi import YTMusic

class Song:
    def __init__(self, title: str, artist: str, duration: int, bpm: int, genre: str):
        self.title = title
        self.artist = artist
        self.duration = duration  # in seconds
        self.bpm = bpm
        self.genre = genre

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.duration//60}:{self.duration%60:02d})"

class WorkoutPlaylist:
    def __init__(self):
        self.songs: List[Song] = []
        self.api_client = None  # Initialize api_client to None
        self.load_song_database()

    def load_song_database(self):
        if self.api_client:
            # TODO: Implement fetching songs from the chosen API
            pass
        else:
            # Use the existing sample database
            self.song_database = [
                Song("Eye of the Tiger", "Survivor", 240, 109, "rock"),
                Song("Stronger", "Kanye West", 312, 104, "hip-hop"),
                Song("Thunderstruck", "AC/DC", 292, 133, "rock"),
                Song("Till I Collapse", "Eminem", 297, 171, "hip-hop"),
                Song("Shake It Off", "Taylor Swift", 219, 160, "pop"),
                Song("Lose Yourself", "Eminem", 326, 171, "hip-hop"),
                Song("Sweet Dreams", "Eurythmics", 216, 125, "pop"),
                Song("Don't Stop Believin'", "Journey", 250, 119, "rock"),
                Song("Pump It", "Black Eyed Peas", 213, 154, "pop"),
                Song("Run the World", "Beyoncé", 236, 127, "pop"),
            ]

    def set_api_client(self, service: str):
        if service == 'spotify':
            self.api_client = SpotifyClient()
        elif service == 'apple_music':
            self.api_client = AppleMusicClient()
        elif service == 'youtube_music':
            self.api_client = YouTubeMusicClient()

    def generate_playlist(
        self,
        workout_type: str,
        duration_minutes: int,
        preferred_genres: List[str] = None,
        min_bpm: Optional[int] = None,
        max_bpm: Optional[int] = None
    ) -> List[Song]:
        """
        Generate a workout playlist based on user preferences
        """
        # Define BPM ranges for different workout types if not specified
        workout_bpm_ranges = {
            "warmup": (90, 120),
            "cardio": (120, 140),
            "hiit": (140, 180),
            "strength": (110, 130),
            "cooldown": (80, 110),
            "yoga": (70, 100)
        }

        if min_bpm is None or max_bpm is None:
            min_bpm, max_bpm = workout_bpm_ranges.get(workout_type.lower(), (100, 140))

        # Filter songs based on criteria
        suitable_songs = [
            song for song in self.song_database
            if min_bpm <= song.bpm <= max_bpm
            and (preferred_genres is None or song.genre in preferred_genres)
        ]

        if not suitable_songs:
            # If no songs match the criteria, gradually expand the BPM range
            bpm_range_expansion = 10
            while not suitable_songs and (min_bpm > 60 or max_bpm < 180):
                min_bpm = max(60, min_bpm - bpm_range_expansion)
                max_bpm = min(180, max_bpm + bpm_range_expansion)
                suitable_songs = [
                    song for song in self.song_database
                    if min_bpm <= song.bpm <= max_bpm
                    and (preferred_genres is None or song.genre in preferred_genres)
                ]
            
            if not suitable_songs:
                # If still no songs, ignore BPM and only consider genre
                suitable_songs = [
                    song for song in self.song_database
                    if preferred_genres is None or song.genre in preferred_genres
                ]
                
            if not suitable_songs:
                # If still no songs, use all available songs
                suitable_songs = self.song_database

        # Create playlist
        playlist = []
        total_duration = 0
        target_duration = duration_minutes * 60

        while total_duration < target_duration and suitable_songs:
            # Choose a random song that fits within remaining time
            remaining_time = target_duration - total_duration
            possible_songs = [s for s in suitable_songs if s.duration <= remaining_time]
            
            if not possible_songs:
                # If no songs fit, choose the shortest available song
                possible_songs = sorted(suitable_songs, key=lambda s: s.duration)
                if possible_songs:
                    selected_song = possible_songs[0]
                else:
                    break
            else:
                selected_song = random.choice(possible_songs)

            playlist.append(selected_song)
            total_duration += selected_song.duration
            suitable_songs.remove(selected_song)

        return playlist

    def save_playlist(self, playlist: List[Song], filename: str):
        """Save playlist to a JSON file"""
        playlist_data = [{
            "title": song.title,
            "artist": song.artist,
            "duration": song.duration,
            "bpm": song.bpm,
            "genre": song.genre
        } for song in playlist]

        with open(filename, 'w') as f:
            json.dump(playlist_data, f, indent=2)

    def load_playlist(self, filename: str) -> List[Song]:
        """Load playlist from a JSON file"""
        with open(filename, 'r') as f:
            playlist_data = json.load(f)
            
        return [Song(**song_data) for song_data in playlist_data]

    def share_playlist(self, playlist: List[Song], platform: str):
        """
        TODO: Implement playlist sharing functionality
        This method will allow users to share their playlists on various platforms
        """
        pass  # Placeholder for future implementation

class SpotifyClient:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private"))

    def search_songs(self, query: str, limit: int = 10) -> List[Song]:
        results = self.sp.search(q=query, limit=limit, type='track')
        songs = []
        for track in results['tracks']['items']:
            song = Song(
                title=track['name'],
                artist=track['artists'][0]['name'],
                duration=track['duration_ms'] // 1000,
                bpm=0,  # Spotify API doesn't provide BPM directly
                genre=""  # Spotify API doesn't provide genre directly
            )
            songs.append(song)
        return songs

class AppleMusicClient:
    def __init__(self):
        # TODO: Implement Apple Music API client
        # You'll need to set up Apple Music API credentials
        pass

    def search_songs(self, query: str, limit: int = 10) -> List[Song]:
        # TODO: Implement song search using Apple Music API
        # This is a placeholder implementation
        return []

class YouTubeMusicClient:
    def __init__(self):
        self.ytmusic = YTMusic()

    def search_songs(self, query: str, limit: int = 10) -> List[Song]:
        results = self.ytmusic.search(query, filter="songs", limit=limit)
        songs = []
        for track in results:
            song = Song(
                title=track['title'],
                artist=track['artists'][0]['name'],
                duration=int(track['duration_seconds']),
                bpm=0,  # YouTube Music API doesn't provide BPM
                genre=""  # YouTube Music API doesn't provide genre directly
            )
            songs.append(song)
        return songs

def format_playlist(playlist: List[Song]) -> str:
    """Format playlist for display"""
    total_duration = sum(song.duration for song in playlist)
    formatted = f"Workout Playlist (Total Duration: {total_duration//60}:{total_duration%60:02d})\n"
    formatted += "-" * 50 + "\n"
    
    for i, song in enumerate(playlist, 1):
        formatted += f"{i}. {song}\n"
    
    return formatted

def get_user_input():
    workout_type = input("Enter workout type (e.g., hiit, yoga, cardio): ").lower()
    duration_minutes = int(input("Enter workout duration in minutes: "))
    genres = input("Enter preferred genres (comma-separated, or press Enter for all): ")
    preferred_genres = [g.strip() for g in genres.split(",")] if genres else None
    min_bpm = input("Enter minimum BPM (or press Enter for default): ")
    max_bpm = input("Enter maximum BPM (or press Enter for default): ")
    
    min_bpm = int(min_bpm) if min_bpm else None
    max_bpm = int(max_bpm) if max_bpm else None
    
    return workout_type, duration_minutes, preferred_genres, min_bpm, max_bpm

def choose_music_service():
    print("Choose a music source:")
    print("1. Local database (demo)")
    print("2. Spotify")
    print("3. Apple Music")
    print("4. YouTube Music")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        return None
    elif choice == '2':
        return 'spotify'
    elif choice == '3':
        return 'apple_music'
    elif choice == '4':
        return 'youtube_music'
    else:
        print("Invalid choice. Using local database.")
        return None

def main():
    generator = WorkoutPlaylist()
    
    # Ask for music source choice every time the script runs
    service = choose_music_service()
    if service:
        generator.set_api_client(service)
    
    while True:
        try:
            workout_type, duration_minutes, preferred_genres, min_bpm, max_bpm = get_user_input()
            
            playlist = generator.generate_playlist(
                workout_type=workout_type,
                duration_minutes=duration_minutes,
                preferred_genres=preferred_genres,
                min_bpm=min_bpm,
                max_bpm=max_bpm
            )
            
            print(f"\n{workout_type.capitalize()} Workout Playlist:")
            print(format_playlist(playlist))
            
            save_option = input("Do you want to save this playlist? (y/n): ").lower()
            if save_option == 'y':
                filename = input("Enter filename to save (e.g., my_playlist.json): ")
                generator.save_playlist(playlist, filename)
                print(f"Playlist saved to {filename}")
            
            another = input("Generate another playlist? (y/n): ").lower()
            if another != 'y':
                break
        
        except ValueError as e:
            print(f"Error: {e}")
        except FileNotFoundError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
