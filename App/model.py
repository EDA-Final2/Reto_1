from datetime import datetime
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog() -> dict:
    """
    Initialize the catalog of artists, albums and tracks
    """

    catalog = {
        "artists": None,
        "albums": None,
        "tracks": None,
    }

    catalog["artists"] = lt.newList("ARRAY_LIST", key="id")
    catalog["albums"] = lt.newList("ARRAY_LIST", key="id")
    catalog["tracks"] = lt.newList("ARRAY_LIST", key="id")

    return catalog


# Funciones para agregar informacion al catalogo


def addArtist(catalog, artist):
    """
    Add an Artist to the List of Artists
    """
    id = artist["id"]
    track_id = artist["track_id"]
    artist_popularity = float(artist["artist_popularity"])
    genres = str(artist["genres"]).replace(
        "[", "").replace("]", "").replace("'", "").split(", ")
    name = artist["name"]
    followers = float(artist["followers"])

    artist = newArtist(id, track_id, artist_popularity,
                       genres, name, followers)

    artists = catalog["artists"]
    lt.addLast(artists, artist)

    return catalog


def addAlbum(catalog, album):
    """
    Add an album to the List of Albums
    """
    id = album["id"]
    track_id = album["track_id"]
    total_tracks = float(album["total_tracks"])
    external_urls = album["external_urls"]
    album_type = album["album_type"]
    available_markets = str(album["available_markets"]).replace(
        "[", "").replace("]", "").replace("'", "").split(", ")
    artist_id = album["artist_id"]
    images = album["images"]

    # https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
    # https://www.ibm.com/docs/en/cmofz/10.1.0?topic=SSQHWE_10.1.0/com.ibm.ondemand.mp.doc/arsa0257.htm
    date = album["release_date"]
    if len(date) == 4:
        format = "%Y"
    elif len(date) == 6:
        format = "%b-%y"
    else:
        if date[4] == "/":
            format = "%Y/%m/%d"
        else:
            format = "%Y-%m-%d"
    release_date = datetime.strptime(date, format).year

    name = album["name"]
    release_date_precision = album["release_date_precision"]

    album = newAlbum(id, track_id, total_tracks, external_urls, album_type,
                     available_markets, artist_id, images, release_date, name, release_date_precision)

    albums = catalog["albums"]
    lt.addLast(albums, album)

    return catalog


def addTrack(catalog, track):
    """
    Add a Track to the List of Tracks
    """
    id = track["id"]
    href = track["href"]
    album_id = track["album_id"]
    key = track["key"]
    track_number = float(track["track_number"])
    artists_id = str(track["artists_id"]).replace(
        "[", "").replace("]", "").replace("'", "").split(", ")
    energy = track["energy"]
    loudness = track["loudness"]
    valence = track["valence"]
    danceability = track["danceability"]
    playlist = track["playlist"]
    speechiness = track["speechiness"]
    popularity = float(track["popularity"])
    liveness = track["liveness"]
    tempo = track["tempo"]
    duration_ms = float(track["duration_ms"])
    acousticness = track["acousticness"]
    available_markets = str(track["available_markets"]).replace(
        "[", "").replace("]", "").replace('"', "").replace("'", "").split(", ")
    lyrics = track["lyrics"]
    disc_number = track["disc_number"]
    instrumentalness = track["instrumentalness"]
    preview_url = track["preview_url"]
    name = track["name"]

    track = newTrack(id, href, album_id, key, track_number, artists_id, energy, loudness, valence, danceability, playlist, speechiness,
                     popularity, liveness, tempo, duration_ms, acousticness, available_markets, lyrics, disc_number, instrumentalness, preview_url, name)

    tracks = catalog["tracks"]
    lt.addLast(tracks, track)

    return catalog


# Funciones para creacion de datos

def newArtist(id, track_id, artist_popularity, genres, name, followers):
    artist = {
        "id": id,
        "track_id": track_id,
        "artist_popularity": artist_popularity,
        "genres": genres,
        "name": name,
        "followers": followers
    }

    return artist


def newAlbum(id, track_id, total_tracks, external_urls, album_type, available_markets, artist_id, images, release_date, name, release_date_precision):
    album = {
        "id": id,
        "track_id": track_id,
        "total_tracks": total_tracks,
        "external_urls": external_urls,
        "album_type": album_type,
        "available_markets": available_markets,
        "artist_id": artist_id,
        "images": images,
        "release_date": release_date,
        "name": name,
        "release_date_precision": release_date_precision,
    }

    return album


def newTrack(id, href, album_id, key, track_number, artists_id, energy, loudness, valence, danceability, playlist, speechiness, popularity, liveness, tempo, duration_ms, acousticness, available_markets, lyrics, disc_number, instrumentalness, preview_url, name):
    track = {
        "id": id,
        "href": href,
        "album_id": album_id,
        "key": key,
        "track_number": track_number,
        "artists_id": artists_id,
        "energy": energy,
        "loudness": loudness,
        "valence": valence,
        "danceability": danceability,
        "playlist": playlist,
        "speechiness": speechiness,
        "popularity": popularity,
        "liveness": liveness,
        "tempo": tempo,
        "duration_ms": duration_ms,
        "acousticness": acousticness,
        "available_markets": available_markets,
        "lyrics": lyrics,
        "disc_number": disc_number,
        "instrumentalness": instrumentalness,
        "preview_url": preview_url,
        "name": name,
    }

    return track


"""
class Artist:
    def __init__(self, id, track_id, artist_popularity, genres, name, followers) -> None:
        self.id = id
        self.track_id = track_id
        self.artist_popularity = artist_popularity
        self.genres = genres
        self.name = name
        self.followers = followers

    def __str__(self) -> str:
        return f"{self.name}, {self.artist_popularity}, {self.genres}, {self.followers}"


class Album:
    def __init__(self, id, track_id, total_tracks, external_url, album_type, available_markets, artist_id, images, release_date, name, release_date_precision) -> None:
        self.id = id
        self.track_id = track_id
        self.total_tracks = total_tracks
        self.external_url = external_url
        self.album_type = album_type
        self.available_markets = available_markets
        self.artist_id = artist_id
        self.images = images
        self.release_date = release_date
        self.name = name
        self.release_date_precision = release_date_precision


class Track:
    def __init__(self, id, href, album_id, key, track_number, artists_id, energy, loudness, valence, danceability, playlist, speechiness, popularity, liveness, tempo, duration_ms, acousticness, available_markets, lyrics, disc_number, instrumentalness, preview_url, name) -> None:
        self.id = id
        self.href = href
        self.album_id = album_id
        self.key = key
        self.track_number = track_number
        self.artists_id = artists_id
        self.energy = energy
        self.loudness = loudness
        self.valence = valence
        self.danceability = danceability
        self.playlist = playlist
        self.speechiness = speechiness
        self.popularity = popularity
        self.liveness = liveness
        self.tempo = tempo
        self.duration_ms = duration_ms
        self.acousticness = acousticness
        self.available_markets = available_markets
        self.lyrics = lyrics
        self.disc_number = disc_number
        self.instrumentalness = instrumentalness
        self.preview_url = preview_url
        self.name = name
"""


# Funciones de consulta

def getSize(list):
    """
    Get the number of elements in a list
    """
    return lt.size(list)


def getElement(list, pos):
    """
    Get the element of the position in a list
    """
    return lt.getElement(list, pos)


def getNFirstElements(list, n):
    """
    Given a list get the first n elements
    """
    return lt.subList(list, 1, n)


def getNLastElements(list, n):
    """
    Given a list get the last n elements
    """
    return lt.subList(list, lt.size(list)-n+1, n)


def getAlbumsBetween(catalog, year_init, year_end):
    """
    Given an initial year and a final year return the list of albums released between
    """
    albums = catalog["albums"]
    albums_sorted = sortAlbumsByYear(albums)

    size = lt.size(albums_sorted)

    def binarySearchYearInf(list, target):
        size = lt.size(list)
        low = 1
        high = lt.size(list)

        res = 1

        while low <= high:
            mid = (low + high) // 2

            element_year = lt.getElement(list, mid)["release_date"]

            if element_year < target:
                low = mid + 1
            elif element_year > target:
                high = mid - 1
            else:
                res = mid
                high = mid - 1
        return res

    def binarySearchYearSup(list, target):
        size = lt.size(list)
        low = 1
        high = lt.size(list)

        res = size

        while low <= high:
            mid = (low + high) // 2

            element_year = lt.getElement(list, mid)["release_date"]

            if element_year < target:
                low = mid + 1
            elif element_year > target:
                high = mid - 1
            else:
                res = mid
                low = mid + 1

        return res

    pos_ini = binarySearchYearInf(albums_sorted, year_init)
    pos_fin = binarySearchYearSup(albums_sorted, year_end)

    albums_between = lt.subList(albums_sorted, pos_ini, pos_fin-pos_ini+1)

    return albums_between
    return pos_ini, pos_fin


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpAlbumsByYear(album1, album2):
    if album1["release_date"] < album2["release_date"]:
        return True
    else:
        return False


# Funciones de ordenamiento

def sortAlbumsByYear(albums):
    albums_to_sort = lt.subList(albums, 1, lt.size(albums))
    albums_sorted = sa.sort(albums_to_sort, cmpAlbumsByYear)

    return albums_sorted
