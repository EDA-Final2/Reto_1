﻿import config as cf
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

    sortAlbumsByYear(catalog)
    sortArtistsByPopularity(catalog)


def loadArtists(catalog):
    """
    Load the Artists in the file
    """
    filename = cf.data_dir + "Spotify/spotify-artists-utf8-" + "small.csv"
    file = csv.DictReader(open(filename, encoding="utf-8"))

    for artist in file:
        catalog = model.addArtist(catalog, artist)
        # break


def loadAlbums(catalog):
    """
    Load the Albums in the file
    """
    filename = cf.data_dir + "Spotify/spotify-albums-utf8-" + "small.csv"
    file = csv.DictReader(open(filename, encoding="utf-8"))

    for album in file:
        catalog = model.addAlbum(catalog, album)
        # break


def loadTracks(catalog):
    """
    Load the Tracks in the file
    """
    filename = cf.data_dir + "Spotify/spotify-tracks-utf8-" + "small.csv"
    file = csv.DictReader(open(filename, encoding="utf-8"))

    for track in file:
        catalog = model.addTrack(catalog, track)
        # break


def sortAlbumsByYear(catalog):
    albums = catalog["albums"]
    albums_sorted = model.sortAlbumsByYear(albums)
    catalog["albumsSorted"] = albums_sorted


def sortArtistsByPopularity(catalog):
    artists = catalog["artists"]
    artists_sorted = model.sortArtistsByPopularity(artists)
    catalog["artistsSorted"] = artists_sorted

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo


def getSize(list):
    """
    Get the number of elements in a list
    """
    return model.getSize(list)


def getElement(list, pos):
    """
    Get the element of the position in a list
    """
    return model.getElement(list, pos)


def getValueMap(map, key):
    """
    Get the value of a key in a map
    """
    return model.getValueMap(map, key)


def getAlbumsBetween(catalog, year_init, year_end):
    """
    Given an initial year and a final year return the list of albums released between
    """
    return model.getAlbumsBetween(catalog, year_init, year_end)


def getNFirstElements(list, n):
    """
    Get the n first elements in a list
    """
    return model.getNFirstElements(list, n)


def getTopArtists(catalog, n):
    """
    Get the top n of artists by popularity
    """
    return model.getTopArtists(catalog, n)
