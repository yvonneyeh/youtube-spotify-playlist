"""A program to generate Spotify playlist that adds songs from your liked videos on YouTube."""

# Log into YouTube
# Fetch liked YouTube videos
# Create new Spotify playlist
# Search for song on Spotify
# Add song to new Spotify playlist

import json
import requests
from secrets import spotify_user_id

class Playlist:

    def __self__(self):
        self.user_id = spotify_user_id

    def get_youtube_client(self):
        """Log in to YouTube; return something."""
        pass

    def get_liked_vids(self):
        """Get liked videos from YouTube."""
        pass

    def create_spotify_playlist(self):
        """Create a new Spotify playlist; return playlist ID."""
        pass

        request_body = json.dumps({
          "name": "Liked YouTube Songs",
          "description": "All Liked Songs from YouTube",
          "public": True
        })

        query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = requests.post(query,
                            data = request_body,
                            headers = {
                            "Content-Type":"application/json",
                            "Authorization":f"Bearer {spotify_token}"})
        response_token = response.json()
        # playlist id
        return response_json["id"]

    def get_spotify_uri(self):
        """Search for the song on Spotify."""
        pass

    def add_song(self):
        """Add a song to Spotify playlist."""
        pass
