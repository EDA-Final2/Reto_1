import config as cf
import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Change csv limit

csv.field_size_limit(2147483647)


# Inicialización del Catálogo de libros

def newCatalog():
    """
    Create an instance of the model
    """
    catalog = model.newCatalog()

    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    """
    Call functions to load Artists, Albums, Tracks
    """
    loadArtists(catalog)
    loadAlbums(catalog)
    loadTracks(catalog)

    # return catalog
    # print(catalog)


def loadArtists(catalog):
    """
    Load the Artists in the file
    """
    filename = cf.data_dir + "Spotify/spotify-artists-utf8-" + "small.csv"
    file = csv.DictReader(open(filename, encoding="utf-8"))

    for artist in file:
        catalog = model.addArtist(catalog, artist)
        break


def loadAlbums(catalog):
    """
    Load the Albums in the file
    """
    filename = cf.data_dir + "Spotify/spotify-albums-utf8-" + "small.csv"
    file = csv.DictReader(open(filename, encoding="utf-8"))

    for album in file:
        catalog = model.addAlbum(catalog, album)
        break


def loadTracks(catalog):
    """
    Load the Tracks in the file
    """
    filename = cf.data_dir + "Spotify/spotify-tracks-utf8-" + "small.csv"
    file = csv.DictReader(open(filename, encoding="utf-8"))

    for track in file:
        catalog = model.addTrack(catalog, track)
        break


loadData(catalog=model.newCatalog())


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
