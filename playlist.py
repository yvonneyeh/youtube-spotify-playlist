"""A program to generate Spotify playlist that adds songs from your liked videos on YouTube."""

# Log into YouTube
# Fetch liked YouTube videos
# Create new Spotify playlist
# Search for song on Spotify
# Add song to new Spotify playlist

import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl

from exceptions import ResponseException
from secrets import spotify_token, spotify_user_id


class Playlist:

    def __self__(self):
        self.user_id = spotify_user_id
        self.youtube_client = self.get_youtube_client()
        self.all_song_info = {}

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

    def get_spotify_uri(self, song_name, artist):
        """Search for the song on Spotify."""

        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(song_name,
                        artist)
        response = requests.get(query,
                        headers={
                            "Content-Type": "application/json",
                            "Authorization": "Bearer {}".format(spotify_token)})
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # only use the first song
        uri = songs[0]["uri"]

        return uri

    def add_song(self):
        """Add a song to Spotify playlist."""
        pass
