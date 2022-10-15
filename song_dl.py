import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from creds import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET
from user_info import PLAYLIST_ID

class SongDownload:
    def __init__(self) -> None:
        self.SPOTIPY_CLIENT_ID = SPOTIPY_CLIENT_ID
        self.SPOTIPY_CLIENT_SECRET = SPOTIPY_CLIENT_SECRET
        self.PLAYLIST_ID = PLAYLIST_ID

        auth = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
        self.sp = spotipy.Spotify(client_credentials_manager=auth)

    def get_playlist(self, PLAYLIST_ID):
        sp_songs= self.sp.playlist_tracks(playlist_id=PLAYLIST_ID, fields='items.track.name')

        for song in sp_songs['items']:
            print(song['track']['name'])
        
    def get_folder(self):
        pass

    def check_duplicates(self):
        pass

    def download_songs(self):
        pass

    def rename_files(self):
        pass
    
    def update_metadata(self):
        pass
    
if __name__ == '__main__':
    sdl = SongDownload()
    sdl.get_playlist(PLAYLIST_ID)
