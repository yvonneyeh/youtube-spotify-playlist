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
        """Log in to YouTube, return YouTube client."""

        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # Get YouTube credentials and create API client
        scopes = ["https://www.googleapis.com/auth youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                                            client_secrets_file, scopes)
        credentials = flow.run_console()

        # Youtube DATA API
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        return youtube_client

    def get_liked_vids(self):
        """Get liked videos from YouTube; create dictionary with song info."""

        request = self.youtube_client.videos().list(
                                part="snippet,contentDetails,statistics",
                                myRating="like")
        response = request.execute()

        # Loop through videos to get important information about songs
        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url = "https://www.youtube.com/watch?v={}".format(item["id"])

            # Use youtube_dl to collect song name & artist name
            video = youtube_dl.YoutubeDL({}).extract_info(youtube_url,
                                                        download=False)
            song_name = video["track"]
            artist = video["artist"]

            if song_name is not None and artist is not None:
                # Save song info and skip any missing song/artist
                self.all_song_info[video_title] = {
                    "youtube_url": youtube_url,
                    "song_name": song_name,
                    "artist": artist,

                    # Add the URI, append song to playlist
                    "spotify_uri": self.get_spotify_uri(song_name, artist)

                }

    def create_spotify_playlist(self):
        """Create a new Spotify playlist; return playlist ID."""
        pass

        request_body = json.dumps({
          "name": "Liked YouTube Songs",
          "description": "All Liked Songs from YouTube",
          "public": True })

        query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        response = requests.post(query,
                            data = request_body,
                            headers = {
                            "Content-Type":"application/json",
                            "Authorization":f"Bearer {spotify_token}"})
        response_token = response.json()
        # Playlist ID
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

        # Only use the first song
        uri = songs[0]["uri"]

        return uri

    def add_song(self):
        """Add a song to Spotify playlist."""

        # Populate dictionary with liked songs

        # Collect all URIs

        # Create new playlists

        # Add all songs into new playlists

        # Check for valid response status

        
