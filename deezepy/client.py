import deezepy
import requests
from typing import Union


class Client:
    def __init__(self):
        pass

    def get_track(
        self,
        track_id: Union[int, str],
    ):
        raw_track = self._get(
            'track',
            track_id
        )

        return deezepy.Track(raw_track)

    def get_artist(
        self,
        artist_id: Union[int, str],
    ):
        raw_artist = self._get(
            'artist',
            artist_id
        )

        return deezepy.Artist(raw_artist)

    def get_artist_top_tracks(
        self,
        artist_id: Union[int, str],
        limit: int = 10,
    ):
        raw_top_tracks = self._get(
            'artist',
            f'{artist_id}/top?limit={limit}'
        )

        return [deezepy.Track(track) for track in raw_top_tracks.get('data')]

    def get_artist_albums(
        self,
        artist_id: Union[int, str]
    ):
        raw_albums = self._get(
            'artist',
            f'{artist_id}/albums'
        )

        return [deezepy.Album(album) for album in raw_albums.get('data')]

    def get_album(
        self,
        album_id: Union[int, str]
    ):
        raw_album = self._get(
            'album',
            album_id
        )

        return deezepy.Album(raw_album)

    def get_album_tracks(
        self,
        album_id: Union[int, str]
    ):
        raw_album_tracks = self._get(
            'album',
            f'{album_id}/tracks'
        )

        return [deezepy.Track(track) for track in raw_album_tracks.get('data')]

    def _get(
        self,
        object: str,
        object_id: Union[int, str],
        params: dict = {}
    ):
        params['Content-Type'] = 'application/json'
        r = requests.get(
            f'https://api.deezer.com/{object}/{object_id}',
            params=params
        )

        return r.json()
