import pandas as pd
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
# df = pd.DataFrame([1, 2, 3], columns={'fdfd'})
# print(df.to_markdown(index=False, tablefmt='grid'))


def printMenu():
    """
    Function to print the Menu Options
    """
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Albumes en un periodo de tiempo")

# Functions to show answers


def printUploadData(catalog):
    """
    Print information of the upload of the data
    """

    artists = catalog["artists"]
    albums = catalog["albumsSorted"]
    tracks = catalog["tracks"]

    num_artists = controller.getSize(artists)
    num_albums = controller.getSize(albums)
    num_tracks = controller.getSize(tracks)

    print("-"*30)
    print(f"Artists: \t{num_artists}")
    print(f"Albums: \t{num_albums}")
    print(f"Tracks: \t{num_tracks}")
    print("-"*30)

    first_last_artists = []
    first_last_albums = []
    first_last_tracks = []

    for i in range(1, 4):
        artist = controller.getElement(artists, i)
        first_last_artists.append(artist)

        album = controller.getElement(albums, i)
        first_last_albums.append(album)

        track = controller.getElement(tracks, i)
        first_last_tracks.append(track)

    for i in range(3, 0, -1):
        artist = controller.getElement(artists, num_artists-i+1)
        first_last_artists.append(artist)

        album = controller.getElement(albums, num_albums-i+1)
        first_last_albums.append(album)

        track = controller.getElement(tracks, num_tracks-i+1)
        first_last_tracks.append(track)

    print("\nFirst and last 3 artists are")
    artists_df = pd.DataFrame(first_last_artists)[
        ["name", "artist_popularity", "followers", "genres"]]
    print(artists_df.to_markdown(index=False))

    print("\nFirst and last 3 albums are")
    albums_df = pd.DataFrame(first_last_albums)[
        ["name", "album_type", "release_date"]]
    print(albums_df.to_markdown(index=False))

    print("\nFirst and last 3 tracks are")
    tracks_df = pd.DataFrame(first_last_tracks)[
        ["name", "duration_ms", "track_number"]]
    print(tracks_df.to_markdown(index=False))


def printAlbumsBetween(albums_between, year_init, year_end):
    """
    Print information and the albums between a range
    """
    albums_between_size = controller.getSize(albums_between)

    first_last_albums = []

    if albums_between_size < 7:
        for i in range(1, albums_between_size+1):
            album = controller.getElement(albums_between, i)

            artist_id = album["artist_id"]
            artistsHash = catalog["artistsHash"]

            artist = controller.getValueMap(artistsHash, artist_id)
            album["artist_name"] = "Unknown"
            if artist != "Not Found":
                album["artist_name"] = artist["name"]

            first_last_albums.append(album)

    else:
        for i in range(1, 4):
            album = controller.getElement(albums_between, i)

            artist_id = album["artist_id"]
            artistsHash = catalog["artistsHash"]

            artist = controller.getValueMap(artistsHash, artist_id)
            album["artist_name"] = "Unknown"
            if artist != "Not Found":
                album["artist_name"] = artist["name"]

            first_last_albums.append(album)

        for i in range(3, 0, -1):
            album = controller.getElement(
                albums_between, albums_between_size-i+1)
            artistsHash = catalog["artistsHash"]

            artist = controller.getValueMap(artistsHash, artist_id)
            album["artist_name"] = "Unknown"
            if artist != "Not Found":
                album["artist_name"] = artist["name"]

            first_last_albums.append(album)

    print(
        f"\n{albums_between_size} albums released between {year_init} and {year_end}\n")

    if albums_between_size > 0:

        albums_between_df = pd.DataFrame(first_last_albums)[
            ["name", "release_date", "album_type", "artist_name", "total_tracks"]]

        print(albums_between_df.to_markdown(index=False))


catalog = controller.newCatalog()


"""
Menu principal
"""

while True:

    printMenu()

    inputs = input('\nSeleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        print("\nCargando información de los archivos ....")
        controller.loadData(catalog)

        printUploadData(catalog)

    elif int(inputs[0]) == 2:
        print("\nReq 1.\n"+"-"*20)
        year_init = int(input("Initial Year: "))
        year_end = int(input("Final Year: "))

        albums_between = controller.getAlbumsBetween(
            catalog, year_init, year_end)

        albums_between_size = controller.getSize(albums_between)

        printAlbumsBetween(albums_between, year_init, year_end)

    elif int(inputs[0]) == 3:
        pass

    else:
        print("Saliendo de la Aplicación")
        break
