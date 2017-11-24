from datetime import date
from pony.orm import *


db = Database()


class Song(db.Entity):
    id = PrimaryKey(int, auto=True)
    playlists = Set('Playlist')
    name = Required(str)
    band = Required('Band')
    artists = Set('Artist')
    album = Optional('Album')
    releaseDate = Optional(date)
    genres = Set('Genre')
    lyrics = Optional(str)
    length = Optional(int)
    address = Optional(str)


class Playlist(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    description = Optional(str)
    songs = Set(Song)


class Band(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    artists = Set('Artist')
    albums = Set('Album')
    songs = Set(Song)


class Artist(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    birthDate = Optional(date)
    band = Optional(Band)
    songs = Set(Song)


class Album(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    songs = Set(Song)
    band = Required(Band)
    numberOfSongs = Required(int)


class Genre(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    songs = Set(Song)

#set_sql_debug(True)
# SQLite
db.bind(provider='sqlite', filename='musicly.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

#################################################### SELECT QUERIES ###################################################

@db_session
def getAllPlaylists():
    result = select(p for p in Playlist)[:]
    return result

@db_session
def viewOnePlaylist(playListName):
    result = Playlist.select(lambda p: p.name == playListName)
    return result

@db_session
def viewAlbums():
    result = select(a for a in Album)[:]
    return result

@db_session
def viewArtists():
    result = select(a for a in Artist)[:]
    return result

@db_session
def viewGenres():
    result = select(g for g in Genre)[:]
    return result

@db_session
def viewBands():
    result = select(b for b in Band)[:]
    return result

@db_session
def viewSong(songName):
    result = Song.select(lambda s: s.name == songName)
    return result

#################################################### SELECT QUERIES ###################################################


#################################################### INSERT QUERIES ###################################################

@db_session
def addPlaylist(pName, pDesc):
    newPlaylist = Playlist(name=pName, description=pDesc)
    commit()

@db_session
def addArtist(aName, aBDate, BandId):
    newArtist = Artist(name=aName, birthDate=aBDate, band=Band[BandId])
    commit()
@db_session
def addAlbum(aTitle, BandId):
    newAlbum = Album(title=aTitle, band=Band[BandId])
    commit()

@db_session
def addBand(aName):
    newBand = Band(name=aName)
    commit()
    return newBand


#################################################### INSERT QUERIES ###################################################





def StringPrepere(str):
    while(len(str) <20):
        str +=" "
    return str