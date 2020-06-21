import deezepy

client = deezepy.Client()


class Artist:
    """
    An artist
    """
    def __init__(self, json):
        if not json:
            json = {}

        self.raw = json
        self.id = json.get('id')
        self.name = json.get('name')
        self.link = json.get('link')
        self.pictures = [
            json.get('picture'),
            json.get('picture_small'),
            json.get('picture_medium'),
            json.get('picture_big'),
            json.get('picture_xl')
        ]
        self.total_albums = json.get('nb_albums')
        self.fans = json.get('nb_fan')

    def get_top_tracks(self):
        return client.get_artist_top_tracks(self.id)

    def get_albums(self):
        return client.get_artist_albums(self.id)


class Album:
    """
    An album
    """
    def __init__(self, json):
        if not json:
            json = {}

        self.raw = json
        self.id = json.get('id')
        self.title = json.get('title')
        self.upc = json.get('upc')
        self.link = json.get('link')
        self.covers = [
            json.get('cover'),
            json.get('cover_small'),
            json.get('cover_medium'),
            json.get('cover_big'),
            json.get('cover_xl')
        ]

        if json.get('genres'):
            self.genres = [
                Genre(genre) for genre in json.get('genres').get('data')
            ]
        else:
            self.genres = None

        self.total_tracks = json.get('nb_tracks')
        self.duration = json.get('duration')
        self.fans = json.get('fans')
        self.rating = json.get('rating')
        self.release_date = json.get('release_date')
        self.type = json.get('record_type')
        self.explicit = json.get('explicit_lyrics')

        if json.get('contributors'):
            self.artists = [
                Artist(artist) for artist in json.get('contributors')
            ]
        else:
            self.artists = None

        self.artist = Artist(json.get('artist'))

        if json.get('tracks'):
            self.tracks = [
                Track(track) for track in json.get('tracks').get('data')
            ]
        else:
            self.tracks = None

    def get_tracks(self):
        return client.get_album_tracks(self.id)


class Genre:
    """
    A genre
    """
    def __init__(self, json):
        if not json:
            json = {}

        self.raw = json
        self.id = json.get('id')
        self.name = json.get('name')
        self.pictures = [
            json.get('picture'),
            json.get('picture_small'),
            json.get('picture_medium'),
            json.get('picture_big'),
            json.get('picture_xl')
        ]


class Track:
    """
    A track
    """
    def __init__(self, json):
        if not json:
            json = {}

        self.raw = json
        self.id = json.get('id')
        self.title = json.get('title')
        self.isrc = json.get('isrc')
        self.link = json.get('link')
        self.duration = json.get('duration')
        self.track_position = json.get('track_position')
        self.disk_number = json.get('disk_number')
        self.rank = json.get('rank')
        self.release_date = json.get('release_date')
        self.explicit = json.get('explicit_lyrics')
        self.preview = json.get('preview')
        self.bpm = json.get('bpm')

        if json.get('contributors'):
            self.artists = [
                Artist(artist) for artist in json.get('contributors')
            ]
        else:
            self.artists = None

        self.artist = Artist(json.get('artist'))
        self.album = Album(json.get('album'))
