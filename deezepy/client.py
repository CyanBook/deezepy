import deezepy
from deezepy.errors import (
    QuotaExceeded,
    ItemsLimitExceeded,
    Permission,
    TokenInvalid,
    Parameter,
    ParameterMissing,
    QueryInvalid,
    ServiceBusy,
    DataNotFound,
    IndividualAccountNotAllowed
)

import requests
from typing import Union


class Client:
    """
    Deezepy Client. Use it to access Deezer API and high-level functions
    """

    def __init__(self):
        pass

    def get_album(
        self,
        album_id: Union[int, str]
    ):
        """
        Get info about an album

        Parameters:
            album_id (``int`` | ``str``):
                Unique album's Deezer ID, must be a digit

        Returns:
            :class:`~deezepy.Album` - On success, an album object is returned
        """

        raw_album = self._get(
            'album',
            album_id
        )

        return deezepy.Album(raw_album)

    def get_album_tracks(
        self,
        album_id: Union[int, str]
    ):
        """
        Get tracks of an album

        Parameters:
            album_id (``int`` | ``str``):
                Unique album's Deezer ID, must be a digit

        Returns:
            List of :class:`~deezepy.Track` - On success, a list of track objects is returned
        """

        raw_album_tracks = self._get(
            'album',
            f'{album_id}/tracks'
        )

        return [deezepy.Track(track) for track in raw_album_tracks.get('data')]

    def get_artist(
        self,
        artist_id: Union[int, str],
    ):
        """
        Get info about an artist

        Parameters:
            artist_id (``int`` | ``str``):
                Unique artist's Deezer ID, must be a digit

        Returns:
            :class:`~deezepy.Artist` - On success, an artist object is returned
        """

        raw_artist = self._get(
            'artist',
            artist_id
        )

        return deezepy.Artist(raw_artist)

    def get_artist_top(
        self,
        artist_id: Union[int, str],
        limit: int = 10,
    ):
        """
        Get top tracks of an artist

        Parameters:
            artist_id (``int`` | ``str``):
                Unique artist's Deezer ID, must be a digit

        Returns:
            List of :class:`~deezepy.Track` - On success, a list of track objects is returned
        """

        raw_top_tracks = self._get(
            'artist',
            f'{artist_id}/top?limit={limit}'
        )

        return [deezepy.Track(track) for track in raw_top_tracks.get('data')]

    def get_artist_albums(
        self,
        artist_id: Union[int, str]
    ):
        """
        Get albums of an artist

        Parameters:
            artist_id (``int`` | ``str``):
                Unique artist's Deezer ID, must be a digit

        Returns:
            List of :class:`~deezepy.Album` - On success, a list of album objects is returned
        """

        raw_albums = self._get(
            'artist',
            f'{artist_id}/albums'
        )

        return [deezepy.Album(album) for album in raw_albums.get('data')]

    def get_track(
        self,
        track_id: Union[int, str],
    ):
        """
        Get info about a track

        Parameters:
            track_id (``int`` | ``str``):
                Unique track's Deezer ID, must be a digit

        Returns:
            :class:`~deezepy.Track` - On success, a track object is returned
        """

        raw_track = self._get(
            'track',
            track_id
        )

        return deezepy.Track(raw_track)

    def _get(
        self,
        object: str,
        object_id: Union[int, str],
        params: dict = {}
    ):
        """
        Internal method used to send API requests to Deezer

        Parameters:
            object (``str``):
                Object you want to use

            object_id (``int`` | ``str``):
                Object's ID

            params (``dict``):
                Optional parameters

        Returns:
            ``dict`` - On success, a parsed JSON dict is retuned
        """

        params['Content-Type'] = 'application/json'
        r = requests.get(
            f'https://api.deezer.com/{object}/{object_id}',
            params=params
        )

        r = r.json()
        if r.get("error"):
            error_code = r.get("error").get("code")

            if error_code == 4:
                raise QuotaExceeded
            elif error_code == 100:
                raise ItemsLimitExceeded
            elif error_code == 200:
                raise Permission
            elif error_code == 300:
                raise TokenInvalid
            elif error_code == 500:
                raise Parameter
            elif error_code == 501:
                raise ParameterMissing
            elif error_code == 600:
                raise QueryInvalid
            elif error_code == 700:
                raise ServiceBusy
            elif error_code == 800:
                raise DataNotFound
            elif error_code == 901:
                raise IndividualAccountNotAllowed
