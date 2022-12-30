import pandas as pd
import config as cf
import sys
import controller
import pycountry
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
    print("3- Top de Artistas por Popularidad")
    print("4- Top de Canciones por Popularidad")
    print("5- Canción más popular Artista en Mercado")

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

    if albums_between_size < 6:
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


def printTopArtists(catalog, top_artists, n):
    """
    Print the top n artists by popularity
    """
    top_artists_size = controller.getSize(top_artists)

    first_last_artists = []

    if top_artists_size < 6:
        for i in range(1, top_artists_size+1):
            artist = controller.getElement(top_artists, i)

            track_id = artist["track_id"]
            tracksHash = catalog["tracksHash"]

            track = controller.getValueMap(tracksHash, track_id)
            artist["track_name"] = "Unknown"
            if track != "Not Found":
                artist["track_name"] = track["name"]

            first_last_artists.append(artist)

    else:
        for i in range(1, 4):
            artist = controller.getElement(top_artists, i)

            track_id = artist["track_id"]
            tracksHash = catalog["tracksHash"]

            track = controller.getValueMap(tracksHash, track_id)
            artist["track_name"] = "Unknown"
            if track != "Not Found":
                artist["track_name"] = track["name"]

            first_last_artists.append(artist)

        for i in range(3, 0, -1):
            artist = controller.getElement(top_artists, top_artists_size-i+1)

            track_id = artist["track_id"]
            tracksHash = catalog["tracksHash"]

            track = controller.getValueMap(tracksHash, track_id)
            artist["track_name"] = "Unknown"
            if track != "Not Found":
                artist["track_name"] = track["name"]

            first_last_artists.append(artist)

    print(
        f"\n{top_artists_size} artists on the search of Top {n}\n")
    if top_artists_size > 0:
        top_artists_df = pd.DataFrame(first_last_artists)[
            ["name", "artist_popularity", "followers", "track_name", "genres"]]
        print(top_artists_df.to_markdown(index=False))


def printTopTracks(catalog, top_tracks, n):
    """
    Print the top n Tracks by Popularity
    """
    top_tracks_size = controller.getSize(top_tracks)

    first_last_tracks = []

    if top_tracks_size < 6:
        for i in range(1, top_tracks_size+1):
            track = controller.getElement(top_tracks, i)

            albumsHash = catalog["albumsHash"]
            album_id = track["album_id"]
            album = controller.getValueMap(albumsHash, album_id)

            track["album_name"] = "Unknown"
            if album != "Not Found":
                track["album_name"] = album["name"]

            artistsHash = catalog["artistsHash"]
            artists_id = track["artists_id"]
            artists_name = []
            for id in artists_id:
                artist = controller.getValueMap(artistsHash, id)

                artist_name = "Unknown"
                if artist != "Not Found":
                    artist_name = artist["name"]
                    artists_name.append(artist_name)

            track["artists_name"] = artists_name

            first_last_tracks.append(track)

    else:
        for i in range(1, 4):
            track = controller.getElement(top_tracks, i)

            albumsHash = catalog["albumsHash"]
            album_id = track["album_id"]
            album = controller.getValueMap(albumsHash, album_id)

            track["album_name"] = "Unknown"
            if album != "Not Found":
                track["album_name"] = album["name"]

            artistsHash = catalog["artistsHash"]
            artists_id = track["artists_id"]
            artists_name = []
            for id in artists_id:
                artist = controller.getValueMap(artistsHash, id)

                artist_name = "Unknown"
                if artist != "Not Found":
                    artist_name = artist["name"]
                    artists_name.append(artist_name)

            track["artists_name"] = artists_name

            first_last_tracks.append(track)

        for i in range(3, 0, -1):
            track = controller.getElement(top_tracks, top_tracks_size-i+1)

            albumsHash = catalog["albumsHash"]
            album_id = track["album_id"]
            album = controller.getValueMap(albumsHash, album_id)

            track["album_name"] = "Unknown"
            if album != "Not Found":
                track["album_name"] = album["name"]

            artistsHash = catalog["artistsHash"]
            artists_id = track["artists_id"]
            artists_name = []
            for id in artists_id:
                artist = controller.getValueMap(artistsHash, id)

                artist_name = "Unknown"
                if artist != "Not Found":
                    artist_name = artist["name"]
                    artists_name.append(artist_name)

            track["artists_name"] = artists_name

            first_last_tracks.append(track)

    print(
        f"\n{top_tracks_size} Tracks on the search of Top {n}\n")
    if top_tracks_size > 0:
        top_tracks_df = pd.DataFrame(first_last_tracks)[
            ["name", "album_name", "artists_name", "popularity", "duration_ms"]]
        print(top_tracks_df.to_markdown(index=False))


def printPopularSongArtistMarket(catalog, tracks, artist_name, country_name):

    popular_track = controller.getElement(tracks, 1)

    print(
        f"\n'{artist_name}' most popular song in '{country_name}'\n")

    pop_track_df = pd.DataFrame(popular_track)
    print(popular_track)


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
        print("\nReq 1.\nAlbums on a period\n"+"-"*20)
        year_init = int(input("Initial Year: "))
        year_end = int(input("Final Year: "))

        albums_between = controller.getAlbumsBetween(
            catalog, year_init, year_end)

        printAlbumsBetween(albums_between, year_init, year_end)

    elif int(inputs[0]) == 3:
        print("\nReq 2.\nTop Artists by Popularity\n"+"-"*20)
        n = int(input("Top N: "))

        artist_size = controller.getSize(catalog["artists"])
        if n > artist_size:
            n = artist_size

        top_artists = controller.getTopArtists(catalog, n)

        printTopArtists(catalog, top_artists, n)

    elif int(inputs[0]) == 4:
        print("\nReq 3.\nTop Tracks by Popularity\n"+"-"*20)

        n = int(input("Top N: "))

        tracks_size = controller.getSize(catalog["tracks"])
        if n > tracks_size:
            n = tracks_size

        top_tracks = controller.getTopTracks(catalog, n)

        printTopTracks(catalog, top_tracks, n)

    elif int(inputs[0]) == 5:
        print("\nReq 4.\nMost Popular Track of an Artist on a Market\n"+"-"*20)

        artist_name = input("Artist Name: ")
        country_name = input("Country Name: ")

        artistsNameHash = catalog["artistsNameHash"]
        artist_id = controller.getValueMap(artistsNameHash, artist_name)
        if artist_id == "Not Found":
            artist_name = "Selena Gomez"
            artist_id = controller.getValueMap(artistsNameHash, artist_name)

        artistsHash = catalog["artistsHash"]
        artist = controller.getValueMap(artistsHash, artist_id)

        try:
            country_code = pycountry.countries.search_fuzzy(country_name)[
                0].alpha_2
        except:
            country_code = pycountry.countries.search_fuzzy("United States")[
                0].alpha_2

        # if artist != "Not Found":
        #     artist_id = artist["id"]

        #     key = artist_id + "-" + country_code
        #     tracksArtistMarketHash = catalog["tracksArtistMarketHash"]
        #     tracks = controller.getValueMap(tracksArtistMarketHash, key)

        #     if tracks != "Not Found":
        #         sorted_tracks = controller.sortArtistTracksByPopularity(tracks)

    else:
        print("\nSaliendo de la Aplicación")
        break
